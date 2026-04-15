# LAB Marzo 8 — Calidad de software (trabajo colaborativo)

**Repositorio:** [https://github.com/ElCalvitoConPeloXD/LAB_Marzo8](https://github.com/ElCalvitoConPeloXD/LAB_Marzo8)

Este laboratorio cumple el objetivo del curso: **usar la tecnología necesaria para que varios desarrolladores apliquen cambios sobre el mismo proyecto** (en este caso Git + GitHub), con una **aplicación libre** ya implementada en este repositorio.

| Requisito (tablero) | Cómo se cumple aquí |
|---------------------|---------------------|
| Equipos de 2 o 3 | Se invita al compañero como colaborador del repo (sección 3.1). |
| Varios devs sobre el mismo proyecto | Ramas, commits y (opcional) *Pull Requests* en GitHub. |
| Implementación + documentación paso a paso | App Flask en `app.py` + esta guía. |
| Evaluación 80% demostrativo / 20% documentación | Demo: repo compartido + app corriendo; doc: este `README`. |

**Fechas del laboratorio:** inicio 8 mar · límite 15 mar (2026).

---

## 1. Qué hace la aplicación

- **Stack:** Python 3 + [Flask](https://flask.palletsprojects.com/).
- **Función:** página web que estima el valor de **π** con el método **Monte Carlo** (puntos aleatorios en un cuadrado y proporción dentro del círculo).
- Archivos principales: `app.py`, `templates/index.html`, `static/style.css`.

No requiere base de datos; sirve para demostrar el flujo colaborativo sobre el mismo código.

**Requisitos:** Python 3.10 o superior (recomendado) y conexión a internet solo la primera vez para instalar Flask con `pip`.

---

## 2. Cómo ejecutarla en tu computadora

En la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abre el navegador en **http://127.0.0.1:5000**.

### Uso de la aplicación

1. En el campo **iteraciones**, escribe un número entero (por ejemplo `10000`; valores más altos suelen acercar mejor el resultado a π, pero tardan un poco más).
2. Pulsa **Calcular**.
3. Se muestra una **aproximación de π** basada en la simulación. Cada ejecución puede variar ligeramente porque usa números aleatorios.

---

## 3. Trabajo en equipo con Git y GitHub (paso a paso)

### 3.1 Dueño del repositorio: dar acceso al compañero

1. Entra al repo en GitHub: [LAB_Marzo8](https://github.com/ElCalvitoConPeloXD/LAB_Marzo8).
2. **Settings** → **Collaborators** (o “Collaborators and teams”) → **Add people**.
3. Escribe el **nombre de usuario de GitHub** de tu compañero y envía la invitación.
4. Tu compañero debe **aceptar** el correo o la notificación en GitHub.

Con eso, **los dos pueden clonar, hacer commits y subir cambios** al mismo repositorio (según permisos que dejes; lo habitual es lectura/escritura en el repo).

### 3.2 Cada persona: copiar el proyecto y crear una rama

```bash
git clone https://github.com/ElCalvitoConPeloXD/LAB_Marzo8.git
cd LAB_Marzo8
git checkout -b mi-rama-descriptiva
```

*(Si usas SSH en lugar de HTTPS, el `clone` será `git@github.com:ElCalvitoConPeloXD/LAB_Marzo8.git`.)*

### 3.3 Hacer cambios y subirlos

```bash
# editar archivos (por ejemplo templates o CSS)
git add .
git status
git commit -m "Describe el cambio en una frase"
git push -u origin mi-rama-descriptiva
```

### 3.4 Integrar el trabajo (recomendado para la demo)

1. En GitHub: **Pull requests** → **New pull request** (de `mi-rama-descriptiva` hacia `main`).
2. Revisar y **Merge**.
3. El otro desarrollador en su PC: `git checkout main` y `git pull` para traer los cambios.

### 3.5 Evitar conflictos simples

- Antes de empezar el día: `git checkout main` y `git pull`.
- Acordar quién toca qué archivo si trabajan a la vez, o usar ramas distintas y fusionar con PR.

---

## 4. Qué preparar para la presentación (80% demostrativo)

- Mostrar el **repositorio en GitHub** con **más de un colaborador** o **varios commits** de personas distintas.
- Mostrar **Pull Request** mergeado (opcional pero muy claro para el jurado).
- Ejecutar **`python app.py`** y usar la web en vivo.

---

## 5. Estructura del proyecto

```
LAB_Marzo8/
├── app.py              # Servidor Flask y lógica Monte Carlo
├── requirements.txt    # Dependencias Python
├── templates/
│   └── index.html      # Formulario y resultado
├── static/
│   └── style.css       # Estilos
└── README.md           # Esta documentación
```

---

## Autores / equipo

| Rol | Nombre | GitHub |
|-----|--------|--------|
| Integrante 1 | *(completar)* | [@ElCalvitoConPeloXD](https://github.com/ElCalvitoConPeloXD) |
| Integrante 2 | *(completar)* | *(usuario del compañero)* |

**Institución / asignatura:** Laboratorio de Calidad de software — marzo 2026.

*(Sustituye los “completar” por los datos reales antes de la entrega.)*
