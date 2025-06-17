import os
import gc
from data_processing.utils import get_logger

class Orchestrator:
    def __init__(self, data_access, transforms):
        self.data_access = data_access
        self.transforms = transforms
        self.logger = get_logger(__name__)

    def run(self):
        for batch_files in self.data_access.get_batches_to_process():
            for file_path in batch_files:
                self.logger.info(batch_files)
                self.logger.info(f"Processing file: {file_path}")

                table, _ = self.data_access.get_table(file_path)

                for transform in self.transforms:
                    table_list, metadata = transform.transform(table)
                    if table_list and len(table_list) > 0:
                        table = table_list[0]
                    else:
                        self.logger.info("Transform returned empty, skipping.")
                        return

                output_path = os.path.join(self.data_access.get_output_folder(), os.path.basename(file_path))
                self.data_access.save_table(output_path, table)
                self.logger.info(f"Finished processing and saved: {output_path}")
                del table
                gc.collect()
