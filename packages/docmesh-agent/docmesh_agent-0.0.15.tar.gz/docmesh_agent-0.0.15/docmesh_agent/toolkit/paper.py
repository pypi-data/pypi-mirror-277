from langchain_core.tools import BaseToolkit

from docmesh_agent.tools.base import BaseAgentTool
from docmesh_agent.tools.paper import (
    AddPaperTool,
    GetPaperIdTool,
    GetPaperPDFTool,
    ReadWholePDFTool,
    ReadPartialPDFTool,
    PaperSummaryTool,
)


class PaperToolkit(BaseToolkit):
    entity_name: str

    def get_tools(self) -> list[BaseAgentTool]:
        return [
            AddPaperTool(entity_name=self.entity_name),
            GetPaperIdTool(entity_name=self.entity_name),
            GetPaperPDFTool(entity_name=self.entity_name),
            ReadWholePDFTool(entity_name=self.entity_name),
            ReadPartialPDFTool(entity_name=self.entity_name),
            PaperSummaryTool(entity_name=self.entity_name),
        ]
