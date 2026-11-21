# Data Mining Project

Three tasks: classification, regression, association rules.

| Notebook                             | Task                          | Owners               |
| ------------------------------------ | ----------------------------- | -------------------- |
| `notebooks/1_classification.ipynb` | Customer Churn Prediction     | Sama, Nagham, Mariam |
| `notebooks/2_regression.ipynb`     | Car Price Prediction          | Mostafa, Hazem       |
| `notebooks/3_association.ipynb`    | Product Recommendation System | Marwan, Moaaz        |

Each notebook is split into sections A–G matching the grading criteria. Every section names its owner.

## Setup

```bash
git clone https://github.com/MoaazHF/a.git
cd a
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

**Colab:** in the first cell run

```python
!git clone https://github.com/MoaazHF/a.git
%cd a/notebooks
!pip install -q imbalanced-learn mlxtend ucimlrepo
```

## Datasets

Download the first two into `data/` with exactly these names. The third is fetched by the notebook itself.

| File                        | Source                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `data/churn.csv`          | [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (`WA_Fn-UseC_-Telco-Customer-Churn.csv`)  |
| `data/cars.csv`           | [Vehicle dataset from CarDekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) (`Car details v3.csv`) |
| — (downloaded automatically) | [Online Retail, UCI](https://archive.ics.uci.edu/dataset/352/online+retail), loaded in the notebook via `ucimlrepo` (internet required) |

## Working rules

- `git pull` before you start, commit and push when you stop.
- Notebooks merge badly. Only one person edits a notebook at a time; say so in the group chat before you open it.
- Edit only your own sections.
- Fit scalers, imputers and SMOTE on the training set only, after the split.
- Use `RANDOM_STATE` (42) everywhere a `random_state` is accepted.
- Before pushing: Kernel → Restart & Run All. The notebook must run top to bottom without errors.
