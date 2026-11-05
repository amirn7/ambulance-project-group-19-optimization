# Ambulance Location in Manhattan (Team 19)

IEOR E4004, Columbia University. Team: Amir Normukhamedov, Ziqiao Sun, Yuting Wang, Rui Xie, Yuhao Yao.

We decide where to base a new fleet of ambulances in Manhattan to cover as much crash-related demand as possible within a budget, using a mixed-integer program solved with Gurobi.

## How to run

1. Open the notebooks in the `Notebooks` folder and run them in this order:

| Notebook | What it does | Writes |
|---|---|---|
| `01_traffic_kappa` | Congestion factor for each 6-hour period | `kappa_t.csv` |
| `02_demand_zones` | Crash demand per 500 m zone and period | `zones.gpkg`, `demand_d_it.csv` |
| `03_sites_network` | Candidate sites, road network, which site reaches which zone in 8 minutes | `sites.csv`, `a_ijt.npy`, `L_metres.npy`, `site_dist.npy` |
| `04_optimization_model` | The optimization model, budget curve and plans | none |

2. The first cell of notebook 01 installs every package the project needs. Run it once, then restart the kernel.
3. Run each notebook from inside the `Notebooks` folder. They read and write files in the main project folder, one level above.

Notebook 04 needs a Gurobi licence. The free pip version of Gurobi is too small for this model, so a full licence (free for academic use) is required.

The outputs are saved in each notebook, so the results can be read without re-running anything.

## Data files not included in this repository

Two of the datasets are too large for GitHub, which rejects any file over 100 MB:

| File | Size | Used by |
|---|---|---|
| `Motor_Vehicle_Collisions_-_Crashes_20261014.csv` (NYPD crash records) | about 540 MB | notebook 02 |
| `Automated_Traffic_Volume_Counts_20261104.csv` (NYC DOT traffic counts) | about 275 MB | notebook 01 |

They can be downloaded from our shared Google Drive folder: <https://drive.google.com/drive/folders/1aL-6C9aItTksDQpYASxLxKVzJ7674MCv?usp=drive_link>

They are also available from NYC Open Data as "Motor Vehicle Collisions - Crashes" and "Automated Traffic Volume Counts".

Place both files in the main project folder, the same folder that contains `Notebooks/`. Do not put them inside `Notebooks/`.

These two files are only needed to re-run notebooks 01 and 02. Everything those notebooks produce (`kappa_t.csv`, `zones.gpkg`, `demand_d_it.csv`) is already included, so notebooks 03 and 04 run without them.