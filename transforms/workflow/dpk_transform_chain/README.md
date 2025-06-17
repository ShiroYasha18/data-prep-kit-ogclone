# dpk_transform_chain

A lightweight pure Python orchestration framework for running transformation pipelines 

This package supports:
- ✅ Full in-memory processing
- ✅ Parallel processing: process multiple files or batches concurrently using multiple threads
- ✅ Simple Python API interface (no YAML, no Prefect, no Dask required)

---

## 📦 Package Components
| Module | Description |
|--------|-------------|
| `Orchestrator` | Full in-memory pipeline (small to medium files) |
| `ParallelOrchestrator` | Parallel batch processing in memory |

---

## 🔧 Install

```bash
cd transforms

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate


pip install ".[all]"

cd ../data-process-lib
pip install . 
```

---

## 🔬 Usage Example

```python
from dpk_transform_chain import Orchestrator
from transforms import Docling2ParquetTransform, DocChunkTransform
from data_access import DataAccessLocal

# Instantiate your transforms (fully compatible with existing transform logic)
transform1 = Docling2ParquetTransform(data_files_to_use=[".pdf"], contents_type="text/markdown")
transform2 = DocChunkTransform(chunking_type="li_markdown")

# Instantiate your data access object
data_access = DataAccessLocal(
    input_folder="/Documents",
    output_folder="/Desktop"
)

# Create orchestrator instance (this example uses AutoMode)
orch = Orchestrator(
    data_access=data_access,
    transforms=[transform1, transform2],
)

# Run full pipeline
orch.run()
```

---

## 🔧 API Summary

| Orchestrator | Class |
|--------------|-------|
| Full memory | `Orchestrator(data_access, transforms)` |

---

## 🔬 Running Tests

```bash
pytest tests/
```

Tests are fully mocked and do not require real data files.

---

