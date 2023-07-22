import logging

import fire

from txdnet import llm
from txdnet import utils

logger = logging.getLogger(__name__)


class Commands:
    def extract_drug_moa_graph(
        self,
        model: str = llm.DEFAULT_MODEL,
        input_filename: str = "poc_rituximab_moa.txt",
        output_filename: str = "poc_rituximab_graph_json.txt",
    ) -> None:
        logger.info(
            f"Starting drug MoA extraction (model={model}, input_filename={input_filename}, output_filename={output_filename})"
        )
        with (utils.paths.data / "input" / input_filename).open(
            "r", encoding="utf-8"
        ) as f:
            text = f.read().strip()
        graph_description = llm.retry(llm.chat_completion_from_template)(
            utils.paths.prompts / "drug_moa_graph_description.txt",
            text=text,
        )
        graph_json = llm.retry(llm.chat_completion_from_template)(
            utils.paths.prompts / "drug_moa_graph_json.txt",
            description=graph_description,
        )
        path = utils.paths.data / "output" / output_filename
        with path.open("w", encoding="utf-8") as f:
            f.write(graph_json)
        logger.info(f"Drug MoA extraction extraction complete ({path})")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s|%(levelname)s|%(module)s|%(funcName)s| %(message)s",
    )
    fire.Fire(Commands())
