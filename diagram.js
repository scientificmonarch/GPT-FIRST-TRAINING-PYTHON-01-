flowchart TD

subgraph group_core["Top level"]
  node_repo(("Training repo<br/>root"))
  node_readme["README<br/>doc<br/>[README.md]"]
  node_summary["Synthesis<br/>doc"]
  node_scratch1["Text project<br/>scratch<br/>[text projet.py]"]
  node_scratch2["Veri check<br/>scratch<br/>[veri.py]"]
end

subgraph group_variables["Variables"]
  node_vars["Variables<br/>subsystem"]
  node_var_id["ID sheet<br/>exercise"]
  node_var_profile["User profile<br/>exercise"]
  node_var_intro["Intro card<br/>exercise"]
  node_var_employee["Employee file<br/>exercise"]
  node_var_guess["Guess game<br/>exercise"]
end

subgraph group_conditions["Conditions"]
  node_conds["Conditions<br/>subsystem"]
  node_cond_train1["Training 1<br/>exercise"]
  node_cond_train2["Training 2<br/>exercise"]
  node_cond_access["Access check<br/>exercise"]
  node_cond_grade["School grade<br/>exercise"]
  node_cond_recruit["Recruitment<br/>exercise"]
  node_cond_logic["Logic traps<br/>exercise"]
  node_cond_reason["Guided reasoning<br/>exercise"]
end

subgraph group_loops["Loops"]
  node_loops["Loops<br/>subsystem"]
  node_loop_start["First loop<br/>exercise"]
  node_loop_for["For loop<br/>exercise"]
  node_loop_mult["Times table<br/>exercise"]
  node_loop_list["List loop<br/>exercise"]
  node_loop_while["While loop<br/>exercise"]
end

subgraph group_lists["Lists"]
  node_lists["Lists<br/>subsystem"]
  node_list_basic["List basics<br/>exercise<br/>[listes 1.py]"]
  node_list_ex["List exercise"]
  node_list_passgen["Pass generator"]
  node_list_party["Party pass<br/>[pass soiree.py]"]
end

subgraph group_projects["Mini-projects"]
  node_projects["Mini-projects<br/>subsystem"]
  node_proj_game1["Game 1<br/>[jeu.py]"]
  node_proj_game2["GPT game<br/>[jeu GPT 1.py]"]
  node_proj_gui["Tkinter app"]
end

node_repo -->|"documents"| node_readme
node_repo -->|"documents"| node_summary
node_repo -->|"scratch"| node_scratch1
node_repo -->|"scratch"| node_scratch2
node_repo -->|"contains"| node_vars
node_repo -->|"contains"| node_conds
node_repo -->|"contains"| node_loops
node_repo -->|"contains"| node_lists
node_repo -->|"contains"| node_projects
node_vars -->|"exercise"| node_var_id
node_vars -->|"exercise"| node_var_profile
node_vars -->|"exercise"| node_var_intro
node_vars -->|"exercise"| node_var_employee
node_vars -->|"exercise"| node_var_guess
node_conds -->|"exercise"| node_cond_train1
node_conds -->|"exercise"| node_cond_train2
node_conds -->|"exercise"| node_cond_access
node_conds -->|"exercise"| node_cond_grade
node_conds -->|"exercise"| node_cond_recruit
node_conds -->|"exercise"| node_cond_logic
node_conds -->|"exercise"| node_cond_reason
node_loops -->|"exercise"| node_loop_start
node_loops -->|"exercise"| node_loop_for
node_loops -->|"exercise"| node_loop_mult
node_loops -->|"exercise"| node_loop_list
node_loops -->|"exercise"| node_loop_while
node_lists -->|"exercise"| node_list_basic
node_lists -->|"exercise"| node_list_ex
node_lists -->|"utility"| node_list_passgen
node_lists -->|"utility"| node_list_party
node_projects -->|"project"| node_proj_game1
node_projects -->|"project"| node_proj_game2
node_projects -->|"project"| node_proj_gui
node_vars -.->|"progresses to"| node_conds
node_conds -.->|"progresses to"| node_loops
node_loops -.->|"progresses to"| node_lists
node_lists -.->|"progresses to"| node_projects

click node_readme "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/README.md"
click node_summary "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/synthese_apprentissage_python.md"
click node_scratch1 "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/text projet.py"
click node_scratch2 "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/veri.py"
click node_var_id "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/4-Variables/Petite fiche d'identité.py"
click node_var_profile "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/4-Variables/Profil utilisateur cm modifié.py"
click node_var_intro "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/4-Variables/Présentation simple cm modifié.py"
click node_var_employee "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/4-Variables/Défis fiche employé complète.py"
click node_var_guess "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/4-Variables/projet python 01 devinette.py"
click node_cond_train1 "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/conditions training leçon1.py"
click node_cond_train2 "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/condition training leçon2.py"
click node_cond_access "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/Exercice 01 contôle d'accès.py"
click node_cond_grade "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/Exercice 03 Mention scolaire.py"
click node_cond_recruit "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/Exercice 07 système complet de recrutement.py"
click node_cond_logic "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/NIVEAU 2 PIEGE LOGIQUE exo1.py"
click node_cond_reason "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/3-conditions/EXERCICE DE RAISONNEMENT PROGRESSIF.py"
click node_loop_start "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/2-Boucles/BOUCLES  PREMIER TEST.py"
click node_loop_for "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/2-Boucles/Boucle ( for ) multiplication.py"
click node_loop_mult "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/2-Boucles/Boucle for et multiplication.py"
click node_loop_list "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/2-Boucles/Boucle list exercice GPT.py"
click node_loop_while "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/2-Boucles/Boucle while exercice.py"
click node_list_basic "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/LISTES/listes 1.py"
click node_list_ex "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/LISTES/exercice liste GPT.py"
click node_list_passgen "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/LISTES/generateur de pass.py"
click node_list_party "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/LISTES/pass soiree.py"
click node_proj_game1 "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/première création/jeu.py"
click node_proj_game2 "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/première création/jeu GPT 1.py"
click node_proj_gui "https://github.com/scientificmonarch/gpt-first-training-python-01-/blob/main/première création/Python projet avec thinker.py"

classDef toneNeutral fill:#f8fafc,stroke:#334155,stroke-width:1.5px,color:#0f172a
classDef toneBlue fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#172554
classDef toneAmber fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#78350f
classDef toneMint fill:#dcfce7,stroke:#16a34a,stroke-width:1.5px,color:#14532d
classDef toneRose fill:#ffe4e6,stroke:#e11d48,stroke-width:1.5px,color:#881337
classDef toneIndigo fill:#e0e7ff,stroke:#4f46e5,stroke-width:1.5px,color:#312e81
classDef toneTeal fill:#ccfbf1,stroke:#0f766e,stroke-width:1.5px,color:#134e4a
class node_repo,node_readme,node_summary,node_scratch1,node_scratch2 toneBlue
class node_vars,node_var_id,node_var_profile,node_var_intro,node_var_employee,node_var_guess toneAmber
class node_conds,node_cond_train1,node_cond_train2,node_cond_access,node_cond_grade,node_cond_recruit,node_cond_logic,node_cond_reason toneMint
class node_loops,node_loop_start,node_loop_for,node_loop_mult,node_loop_list,node_loop_while toneRose
class node_lists,node_list_basic,node_list_ex,node_list_passgen,node_list_party toneIndigo
class node_projects,node_proj_game1,node_proj_game2,node_proj_gui toneTeal