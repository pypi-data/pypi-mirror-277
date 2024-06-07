import re
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Callable, Optional

import pandas as pd
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseLanguageModel
from langchain_core.runnables import RunnableConfig

from docugami_langchain.agents.models import (
    Citation,
    CitationType,
    CitedAnswer,
    Invocation,
)
from docugami_langchain.chains.querying import (
    DocugamiExplainedSQLQueryChain,
    SQLFixupChain,
    SQLQueryExplainerChain,
    SQLResultChain,
)
from docugami_langchain.chains.types.data_type_detection_chain import (
    DataTypeDetectionChain,
)
from docugami_langchain.chains.types.date_parse_chain import DateParseChain
from docugami_langchain.chains.types.float_parse_chain import FloatParseChain
from docugami_langchain.chains.types.int_parse_chain import IntParseChain
from docugami_langchain.config import BATCH_SIZE, MAX_PARAMS_CUTOFF_LENGTH_CHARS
from docugami_langchain.tools.common import NOT_FOUND, BaseDocugamiTool
from docugami_langchain.utils.sql import get_table_info_as_list


class CustomReportRetrievalTool(BaseDocugamiTool):
    """A Tool that knows how to do query a report."""

    name: str = "report_answer_tool"
    description: str = ""

    chain: DocugamiExplainedSQLQueryChain
    report_name: str = ""

    def update(self) -> None:
        """Updates internal state for this tool"""
        self.name = report_name_to_report_query_tool_function_name(self.report_name)
        self.description = report_details_to_report_query_tool_description(
            self.report_name, get_table_info_as_list(self.chain.sql_result_chain.db)
        )

    def to_human_readable(self, invocation: Invocation) -> str:
        if self._is_sql_like(invocation.tool_input):
            return "Querying report."
        else:
            return f"Querying report: {invocation.tool_input}"

    def _is_sql_like(self, question: str) -> bool:
        question = question.lower().strip()
        return question.startswith("select") and "from" in question

    def _run(
        self,
        question: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> CitedAnswer:  # type: ignore
        """Use the tool."""

        if self._is_sql_like(question):
            return CitedAnswer(
                source=self.name,
                answer="Looks like you passed in a SQL query. This tool takes natural language questions, and automatically translates them to SQL queries. "
                "Please try again with a natural language version of this question.",
            )

        try:
            config = None
            if run_manager:
                config = RunnableConfig(
                    run_name=self.__class__.__name__,
                    callbacks=run_manager,
                )

            chain_response = self.chain.run(
                question=question,
                config=config,
            )
            if chain_response.value:
                results = chain_response.value.get("result")
                if results:
                    sql_result = results.get("sql_result") or ""
                    sql_query = results.get("sql_query") or ""
                    explained_sql_query = results.get("explained_sql_query") or ""
                    if sql_result:
                        return CitedAnswer(
                            source=self.name,
                            answer=f"Internally executed query '{sql_query}' which returned '{sql_result}'",
                            citations=(
                                [
                                    Citation(
                                        label=explained_sql_query,
                                        citation_type=CitationType.REPORT,
                                        report_query=sql_query,
                                    )
                                ]
                                if explained_sql_query
                                else []
                            ),
                        )

            return CitedAnswer(source=self.name, answer=NOT_FOUND)
        except Exception as exc:
            return CitedAnswer(
                source=self.name,
                answer=f"There was an error. Please try a different question, or a different tool. Details: {exc}",
            )


def report_name_to_report_query_tool_function_name(name: str) -> str:
    """
    Converts a report name to a report query tool function name.

    Report query tool function names follow these conventions:
    1. Report tool function names always start with "report_answer_tool_".
    2. The rest of the name should be a lowercased string, with underscores
       for whitespace.
    3. Exclude any characters other than a-z (lowercase) from the function name,
       replacing them with underscores.
    4. The final function name should not have more than one underscore together.

    >>> report_name_to_report_query_tool_function_name('Earnings Calls')
    'report_answer_tool_earnings_calls'
    >>> report_name_to_report_query_tool_function_name('COVID-19   Statistics')
    'report_answer_tool_covid_19_statistics'
    >>> report_name_to_report_query_tool_function_name('2023 Market Report!!!')
    'report_answer_tool_2023_market_report'
    """
    # Replace non-letter characters with underscores and remove extra whitespaces
    name = re.sub(r"[^a-z\d]", "_", name.lower())
    # Replace whitespace with underscores and remove consecutive underscores
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"_{2,}", "_", name)
    name = name.strip("_")

    return f"report_answer_tool_{name}"


def report_details_to_report_query_tool_description(name: str, table_info: str) -> str:
    """
    Converts a set of chunks to a direct retriever tool description.
    """
    description = (
        "Pass the COMPLETE question as input to this tool. "
        + f"It implements logic to to answer questions by querying the {name} report and outputs only the answer to your question. "
        + "Use this tool if you think the answer can be calculated from the information in this report via standard data operations like "
        + f"filtering, counting, sorting, averaging or summing.\n\n{table_info}"
    )

    # Cap to avoid runaway tool descriptions.
    return description[:MAX_PARAMS_CUTOFF_LENGTH_CHARS]


def excel_to_sqlite_connection(io: Any, table_name: str) -> str:
    # Create a temporary SQLite database file
    temp_db_file = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
    conn = sqlite3.connect(temp_db_file.name)

    # Read the Excel file using pandas (only the first sheet)
    df = pd.read_excel(io, sheet_name=0)

    # Ignore non-informational columns
    DROP_COLUMNS = ["FileId", "File", "Link to Document"]
    for col in DROP_COLUMNS:
        if col in df.columns:
            df = df.drop(columns=[col])

    # Write the table to the SQLite database
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    return temp_db_file.name


def connect_to_db(db_file_path: str) -> SQLDatabase:
    return SQLDatabase.from_uri(
        f"sqlite:///{db_file_path}",
        sample_rows_in_table_info=0,  # We select and insert sample rows using custom logic
    )


def connect_to_excel(io: Any, table_name: str) -> SQLDatabase:
    db_file_path = excel_to_sqlite_connection(io, table_name)
    return connect_to_db(db_file_path)


def get_retrieval_tool_for_report(
    io: Any,
    report_name: str,
    sql_llm: BaseLanguageModel,
    general_llm: BaseLanguageModel,
    embeddings: Embeddings,
    sql_fixup_examples_file: Optional[Path] = None,
    sql_examples_file: Optional[Path] = None,
    data_type_detection_examples_file: Optional[Path] = None,
    date_parse_examples_file: Optional[Path] = None,
    float_parse_examples_file: Optional[Path] = None,
    int_parse_examples_file: Optional[Path] = None,
    batch_size: int = BATCH_SIZE,
    optimization_completion_callback: Optional[
        Callable[[bool, Optional[Exception]], None]
    ] = None,
) -> BaseDocugamiTool:

    def on_optimization_complete(success: bool, exception: Optional[Exception]) -> None:
        # Update tool (in parent context)
        tool.update()

        # Notify caller, if callback set
        if optimization_completion_callback:
            optimization_completion_callback(success, exception)

    db = connect_to_excel(io, report_name)

    fixup_chain = SQLFixupChain(llm=sql_llm, embeddings=embeddings)
    if sql_fixup_examples_file:
        fixup_chain.load_examples(sql_fixup_examples_file)

    sql_result_chain = SQLResultChain(
        llm=sql_llm,
        embeddings=embeddings,
        db=db,
        sql_fixup_chain=fixup_chain,
    )
    if sql_examples_file:
        sql_result_chain.load_examples(sql_examples_file)

    detection_chain = DataTypeDetectionChain(llm=general_llm, embeddings=embeddings)
    if data_type_detection_examples_file:
        detection_chain.load_examples(data_type_detection_examples_file)

    date_parse_chain = DateParseChain(llm=general_llm, embeddings=embeddings)
    if date_parse_examples_file:
        date_parse_chain.load_examples(date_parse_examples_file)

    float_parse_chain = FloatParseChain(llm=general_llm, embeddings=embeddings)
    if float_parse_examples_file:
        float_parse_chain.load_examples(float_parse_examples_file)

    int_parse_chain = IntParseChain(llm=general_llm, embeddings=embeddings)
    if int_parse_examples_file:
        int_parse_chain.load_examples(int_parse_examples_file)

    sql_result_chain.optimize(
        detection_chain=detection_chain,
        date_parse_chain=date_parse_chain,
        float_parse_chain=float_parse_chain,
        int_parse_chain=int_parse_chain,
        batch_size=batch_size,
        completion_callback=on_optimization_complete,
    )

    sql_query_explainer_chain = SQLQueryExplainerChain(
        llm=general_llm,
        embeddings=embeddings,
    )
    if sql_examples_file:
        sql_query_explainer_chain.load_examples(sql_examples_file)

    tool = CustomReportRetrievalTool(
        chain=DocugamiExplainedSQLQueryChain(
            llm=general_llm,
            embeddings=embeddings,
            sql_result_chain=sql_result_chain,
            sql_query_explainer_chain=sql_query_explainer_chain,
        ),
        report_name=report_name,
    )
    tool.update()

    return tool
