# 💊🧠 DataCon2025 | Drug Discovery: Generation of HDAC6 inhibitors for the treatment of Alzheimer's disease

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.txt)  
[![REINVENT4](https://img.shields.io/badge/REINVENT-4-purple.svg)](https://github.com/MolecularAI/REINVENT4)

## 📁Project structure

- [Final presentation](./docs/Презентация_Datacon_2025_Группа_симметрии.pptx)  
- [ITMO lectures and presentations](./docs/lectures/)  
- [Useful scripts from ITMO](./exps/oth_ipynb/)  
- [Tasks description](./docs/tasks.md)  
- [Mini-tasks](./exps/mini_tasks/)  
- [Data](./data/)  
- [REINVENT4 configurations](./configs/)  
- [Dependencies](requirements.md)  
- [Documentation templates for preprints and articles](./TechDocs/)  
- [Scripts for working with documentation](./tools/)  

<details>
   <summary>Full</summary>

```md
├── 📄 .gitattributes
├── 📄 .gitignore
├── 📄 .gitmodules
├── 📄 LICENSE.txt
├── 📄 README.md
├── 📁 TechDocs
│   ├── 📁 preprint_01
│   └── 📁 scientific_article
├── 📁 configs
│   ├── 📄 REINVENT4_data_pipeline_config.toml
│   ├── 📄 REINVENT4_sampling_config.toml
│   └── 📄 REINVENT4_scoring_config.toml
├── 📁 data
│   ├── 📄 8qa7.pdb
│   ├── 📄 HDAC6 screening dataset using tau-based substrate in an enzymatic assay yields selective inhibitors and activators.xlsx
│   ├── 📄 HDAC6_clean.csv
│   ├── 📄 HDAC6_clean_full.csv
│   ├── 📄 HDAC6_cleaned.csv
│   ├── 📄 HDAC6_filtered.csv
│   ├── 📄 HDAC6_score.csv
│   ├── 📄 REINVENT4_mol2mol_hdac6_active.smi
│   ├── 📄 nastyaleksa04_predictions_hdac6_1.csv
│   ├── 📄 new_molecules__target_cox2_pIC50__descriptors_with_ECFP6.csv
│   ├── 📄 new_molecules__target_cox2_pIC50__smiles.csv
│   ├── 📄 padel_input.smi
│   ├── 📄 padel_output.csv
│   ├── 📁 sampling_out
│   │   ├── 📁 DRAGONFLY
│   │   │   ├── 📄 HDAC6_smiles.csv
│   │   │   ├── 📄 HDAC6_smiles_10.csv
│   │   │   ├── 📄 HDAC6_smiles_10k.csv
│   │   │   ├── 📄 HDAC6_smiles_11.csv
│   │   │   ├── 📄 HDAC6_smiles_2.csv
│   │   │   ├── 📄 HDAC6_smiles_3.csv
│   │   │   ├── 📄 HDAC6_smiles_4.csv
│   │   │   ├── 📄 HDAC6_smiles_5.csv
│   │   │   ├── 📄 HDAC6_smiles_50K_2.csv
│   │   │   ├── 📄 HDAC6_smiles_6.csv
│   │   │   ├── 📄 HDAC6_smiles_7.csv
│   │   │   ├── 📄 HDAC6_smiles_8.csv
│   │   │   ├── 📄 HDAC6_smiles_9.csv
│   │   │   ├── 📄 HDAC6_smiles_only50k.csv
│   │   │   └── 📄 Hdac6_smiles_only.csv
│   │   └── 📁 REINVENT4
│   │       ├── 📄 sampling_out0.csv
│   │       ├── 📄 sampling_out1.csv
│   │       └── 📄 sampling_out2.csv
│   ├── 📄 target_cox2_IC50__descriptors_with_ECFP6.csv
│   ├── 📄 target_cox2_IC50__preprocessed_aggregated.csv
│   ├── 📄 target_cox2_IC50_full_features.csv
│   ├── 📄 trichostatinA.pdbqt
│   └── 📄 trichostatinA.sdf
├── 📁 docs
│   ├── 📄 REINVENT4_interpretations.md
│   ├── 📁 lectures
│   │   ├── 📁 General
│   │   │   ├── 📄 Chemical Space in Drug Discovery.mp4
│   │   │   ├── 📄 Introduction to Medical Chemistry.mp4
│   │   │   └── 📁 Presentations
│   │   │       ├── 📄 Chemical Space in Drug Discovery.pdf
│   │   │       └── 📄 Introduction to Medical Chemistry.pptx
│   │   ├── 📁 for_Chemists
│   │   │   ├── 📄 Chemical libraries.mp4
│   │   │   ├── 📄 Data collection and processing.mp4
│   │   │   ├── 📄 Machine learning algorithms.mp4
│   │   │   ├── 📄 Neural networks.mp4
│   │   │   └── 📁 Presentations
│   │   │       ├── 📄 Chemical libraries.pdf
│   │   │       ├── 📄 Data collection and processing.pptx
│   │   │       ├── 📄 Machine learning.pdf
│   │   │       └── 📄 Neural networks.pdf
│   │   └── 📁 for_ML_spec
│   │       ├── 📄 AutoML.mp4
│   │       ├── 📄 Models for generating molecules.mp4
│   │       ├── 📄 Nanopore sequencing.mp4
│   │       ├── 📄 Nuances of ML in the chemical domain.mp4
│   │       ├── 📁 Presentations
│   │       │   ├── 📄 Generative models.pptx
│   │       │   ├── 📄 Models for generating molecules.pptx
│   │       │   ├── 📄 Nuances of ML in the chemical domain.pdf
│   │       │   └── 📄 Representation of molecules.pdf
│   │       └── 📄 Representation of molecules.mp4
│   ├── 📄 notes.md
│   ├── 📄 targets_comparative_analysis.md
│   ├── 📄 tasks.md
│   └── 📄 Презентация_Datacon_2025_Группа_симметрии.pptx
├── 📁 exps
│   ├── 📄 Filter.ipynb
│   ├── 📄 Prediction.ipynb
│   ├── 📁 mini_tasks
│   │   ├── 📁 catboost_info
│   │   ├── 📄 mini_task_1.ipynb
│   │   ├── 📄 mini_task_2.ipynb
│   │   ├── 📄 mini_task_3.ipynb
│   │   ├── 📄 mini_task_4.ipynb
│   │   ├── 📁 Настя
│   │   │   ├── 📄 task1.ipynb
│   │   │   └── 📄 task2.ipynb
│   │   ├── 📁 Саша
│   │   │   ├── 📄 _mini_task1.ipynb
│   │   │   ├── 📄 _mini_task2.ipynb
│   │   │   ├── 📄 _mini_task3.ipynb
│   │   │   └── 📄 _mini_task4.ipynb
│   │   └── 📁 Ярослав
│   │       ├── 📄 Minitask1.ipynb
│   │       └── 📄 Minitask2.ipynb
│   ├── 📁 models
│   │   ├── 📄 catboost_cox2_model.cbm
│   │   └── 📄 catboost_cox2_model.pkl
│   ├── 📄 nastyaleksa04_Final_task_chemprop.ipynb
│   ├── 📄 nastyaleksa04_Final_task_fingerprints.ipynb
│   ├── 📁 oth_ipynb
│   │   ├── 📄 Machine_learning.ipynb
│   │   ├── 📄 Practice_3_chemists_lecture.ipynb
│   │   ├── 📄 Practice_3_chemists_solution.ipynb
│   │   ├── 📄 chem_data_visuzalisation.ipynb
│   │   ├── 📄 generative_models.ipynb
│   │   └── 📄 pubmed_parser.ipynb
│   ├── 📄 cox2_model_scaler.pkl
│   └── 📄 vendogor_molgen_pipeline.ipynb
├── 📁 img
│   ├── 📄 MAPKpathway.png
│   └── 📄 contributors.png
├── 📁 modules
│   └──> 📁 REINVENT4
├── 📄 requirements.md
├── 📄 requirements.txt
├── 📄 requirements.upd
├── 📄 successful_molecules.csv
└── 📁 tools
    ├── 📁 formatter
    └── 📁 ipynb
```

</details>

## 📋Project description

This project is dedicated to generating new molecules that are potentially capable of interacting with the HDAC6 target, which is involved in the pathogenesis of Alzheimer's disease.  
The project was developed as part of the DataCon2025 competition and uses modern machine learning methods to work with chemical data.

Alzheimer's disease (AD) is one of the most common neurodegenerative diseases, characterized by the formation and deposition of amyloid β (Aβ) plaques in the brain. These plaques trigger a cascade of pathological processes: tau protein hyperphosphorylation → neuroinflammation → neuronal degeneration and cognitive decline.  
Although the amyloid cascade remains one of the leading hypotheses for the pathogenesis of the disease, attempts to develop effective drugs against Aβ have not yet been crowned with significant success, mainly due to the biological complexity of the disease. Current research offers new approaches — from biomarkers and genetic strategies to therapeutic diagnostics — but the need for alternative targets remains extremely relevant.

## 📌Steps

### 1. Target selection🎯

По итогам [сравнительного анализа сигнальных путей](./docs/targets_comparative_analysis.md) и количества доступных данных в открытых базах данных была выбрана целевая мишень:

> [**HDAC6**](https://medach.pro/post/2145)

Гистондеацетилазы (`HDACs`) — это эпигенетические регуляторы, удаляющие ацетильные группы с гистонов и тубулинов. Среди 18 известных изоформ `HDAC` особое внимание привлекает `HDAC6`.  
Исследования показали, что у пациентов с БА наблюдается повышенная экспрессия `HDAC6`, что в свою очередь связано со снижением уровня ацетилированного α-тубулина и нарушением работы нейронов. Более того, `HDAC6` взаимодействуя с тау-белком, способствует его гиперфосфорилированию и формированию нейрофибриллярных клубков (NFTs).

Интерес к ингибиторам `HDAC6` (`HDAC6i`) усилился после того, как в доклинических моделях БА селективные `HDAC6i` продемонстрировали:

- Снижение уровня тау-белка;
- Восстановление аксонального транспорта;
- Улучшение обучаемости и памяти;
- Противовоспалительное действие.

### 2. Datasets and data processing🦜

Для реализации проекта использовалась база данных `BindingDB`, содержащая **10098** молекул, отфильтрованных по `IC50`.  
Именно с неё были выгружены файлы и произведена обработка в 2 этапа:

1) Предварительная подготовка данных, включающая в себя:
   - Обработку пропущенных значений и дубликатов;
   - Проверку корректности молекул по SMILES;
   - Фильтрацию по точности количественных данных, полученных в ходе экспериментов;
   - Фильтрацию по сайту связывания и PDB структурам мишени.

2) Расчет и отбор дескрипторов — производился с использованием библиотек `RDKit` и `Padelpy`:
   - Были рассчитаны молекулярные отпечатки `MACCS Keys` и `Morgan Fingerprints`;
   - Осуществлена фильтрация и отбор признаков с некорректными значениями, нулевой дисперсией и высокой корреляцией ($r > 0.7$ между признаками).

_Также предполагалось использование методов понижения размерности (PCA, PLS, ...), но из-за "химической необоснованности PCA" и сопоставимых метриках качества на разных регрессионных моделях по сравнению с оригинальными данными — было принято решение о пропуске данного этапа и переходу к "обучению"_.

### 3. Training models to predict biological activity📊

На этапе обучения использовались модели `XGBoost` и `ChemProp`.

Для [прогнозирования активности молекул](./exps/Prediction.ipynb) с использованием Fingerprints была обучена модель `XGBoostRegressor`. После оптимизации гиперпараметров с помощью `GridSearchCV` были получены следующие метрики на тестовом наборе данных:

- **$R^2$ (коэффициент детерминации):** $0.657$
- **$\text{MAE}$ (средняя абсолютная ошибка):** $0.423$
- **$\text{RMSE}$ (среднеквадратичная ошибка):** $0.582$

### 4. Molecules generation🔬

Для генерации молекул использовалось несколько моделей:

#### [IDOLpro](https://github.com/sandbox-quantum/idolpro)

Основана на условной диффузионной модели `DiffSBDD-Cond`, учитывающей симметрии SE(3) и обученной генерации лигандов с высокой аффинностью к заданному белковому карману. За 2 ч 40 мин сгенерировать новые лиганды не удалось, поэтому было решено воспользоваться другой моделью.

#### [DRAGONFLY](https://github.com/ETHmodlab/dragonfly_gen)

Глубокая генеративная модель для создания биоактивных молекул по эталонному лиганду или структуре мишени. Использует анализ drug-target interactome, Graph Transformer Neural Network (GTNN) для кодирования и языковую модель на базе RNN-LSTM для генерации SMILES.

Для генерации использовался файл мишени [8qa7.pdb](./data/8qa7.pdb), так как данная структура имеет высокое разрешение $1.47 \text{Å}$. В качестве лиганда использовался [Trichostatin A](./data/trichostatinA.sdf) благодаря высокой аффинности. $\text{IC₅₀} ≈ 10–11 \text{нМ}$ для человеческого и рыбьего `HDAC6`.

В ходе генерация при помощи `DragonFly` в модель одновременно с исходной молекулой подаются значения шести важных молекулярных свойств. Модель генерирует новые SMILES-структуры так, чтобы эти свойства в новых молекулах почти точно совпадали с заданными.

1) Молекулярная масса (Molecular weight)
2) Число вращающихся связей (Rotatable bonds)
3) Число акцепторов водородных связей (H-bond acceptors)
4) Число доноров водородных связей (H-bond donors)
5) Полярная поверхность (Polar surface area, PSA)
6) Липофильность (MolLogP)

Было сгенерировано **121000** новых [SMILES молекул](./data/sampling_out/DRAGONFLY/)

### [REINVENT4](https://github.com/MolecularAI/REINVENT4)

`REINVENT4` — это командная Python-утилита для генерации малых молекул с помощью алгоритмов глубокого обучения и оптимизации через [многокомпонентное вознаграждение](./docs/REINVENT4_interpretations.md).  

- Генераторы представлены в виде **sequence-based** моделей, оперирующих SMILES-строками;
- Базируются на **рекуррентных нейронных сетях (RNN)** и **трансформерах**, обученных моделировать распределение реальных молекулярных SMILES;
- Алгоритм Reinforcement Learning (RL) использует функцию вознаграждения, заданную пользователем как геометрическое среднее нескольких дескрипторов;
- Поддерживается **Transfer Learning (TL)** и **Curriculum Learning (CL)** для тонкой настройки и поэтапного обучения.

**Ключевые возможности:**

- **De novo** дизайн молекул «с нуля»;
- **Mol2Mol** — генерация аналогов, структурно похожих на входные молекулы;
- **Scaffold hopping** — поиск новых каркасов;
- **R-group replacement** — замена заместителей в известных лигандах;
- **Linker design** — проектирование соединителей между фрагментами;
- **Molecule optimization** — улучшение свойств целевых соединений;
- **Плагины** для кастомных scoring-компонентов.

Каждый режим требует соответствующего `.prior` файла и входного набора SMILES (при необходимости). Поддерживаются стохастическая стратегия `multinomial` (с параметром `temperature`) и детерминированная `beamsearch`. Выход сохраняется в CSV с оценкой вероятности (NLL), может быть дополнительно обработан и отсортирован с помощью `scoring`.  

Для [генерации](./configs/REINVENT4_sampling_config.toml) был выбран режим `Mol2Mol`, для которого были отобраны [топ 57 ингибиторов](./data/HDAC6_filtered.csv) `HDAC6`, отсортированных по `pIC50` из общего [очищенного датасета](./data/HDAC6_cleaned.csv)

Итоги генерации в папке [data/sampling_out/REINVENT4/](./data/sampling_out/REINVENT4/)  
Итоги скоринга для [одной из итераций](./data/sampling_out/REINVENT4/sampling_out1.csv) — [data/HDAC6_score.csv](./data/HDAC6_score.csv)  <!-- TODO: Тут нет pIC50 предикта, сматчите колонку из др. файла -->

```python
filtered = cleaned[cleaned["pIC50"] >= 8.7].sort_values(by="pIC50", ascending=False, ignore_index=True)
```

### 5. Molecules filtration🧪

<!-- TODO: ДОПОЛНИТЬ  -->

Сгенерированные молекулы проходили [проверку](./exps/Filter.ipynb) по 6 параметрам:

1) $\text{QED}$ (Quantitative Estimate of Drug-likeness) $>= 0.5$;
2) $\text{SA score}$ (Synthetic Accessibility Score), критерий: $2 < ... < 6$;
3) $\text{Toxicophore}$, критерий: $0$ токсичных фрагментов;
4) $\text{pIC50}$, критерий: $> 6$;
5) Число нарушений 5 правил Липински $<= 1$;
6) BBB (Blood–Brain Barrier) — бинарный признак:
   - `+` (проницаем);
   - `-` (непроницаем).

Молекула проходила отбор успешно, если хотя бы 5 из 6 параметров попадали в допустимые области. Таких молекул было 20 штук.
Дополнительно было принято решение отфильтровать все молекулы с ненулевым Toxicophore. Итого: **10** молекул, из них **1** удовлетворяет всем шести критериям, **9** — пяти.

---

### 🧬TODO: Possible improvements

В дальнейшем предполагается произвести расчеты докинга и молекулярной динамики при появлении требуемых вычислительных ресурсов для понимания карманов связывания, вычислить полный профиль аффинности для всех возможных мишеней с учётом распространенных генетических полиморфизмов исследуемых белков, а также оптимизировать параметры будущих соединений-кандидатов для минимизации нецелевого связывания и тонкой подстройки смещенного ингибирования/(обратной)активации (biased inhibition/(reverse)agonism) конкретных молекулярных цепей, следующих за HDAC6 → ...  
Возможно проведение расчетов взаимодействий с G-белками, очистка данных от выбросов и использование доверительных интервалов, оценка значимости дескрипторов и отбор признаков по p-value, хемоинформатический обоснованная визуализации "химического пространства", добавление QSAR-предиктивной модели в reward + дообучение REINVENT4, оценка общей значимости моделей, добавление штрафов за токсичность по дополнительным метрикам (hERG и прч.), а также интеграция моделей для планирования шагов синтеза в pipeline, наподобие [aizynthfinder](https://github.com/MolecularAI/aizynthfinder).

---

![contributors](./img/contributors.png)
