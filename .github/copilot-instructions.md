## Contexto rápido

Repositorio pequeño de clase: contiene ejemplos y ejercicios en Python. Archivos clave:

- [clase1.py](clase1.py): implementación visible del problema N-reinas. Usa estado global (`tablero`, `columnas`, `diag1`, `diag2`), limpieza de terminal (`os.system('clear')`) y pausas (`time.sleep`) para animación.
- [clase2.py](clase2.py): ejercicios interactivos que piden `input()` y devuelven mensajes. Uso de nombres y comentarios en español.

## Objetivo para un agente AI

Ayudar a mejorar scripts educativos sin romper el comportamiento interactivo en clase. Priorizar cambios no intrusivos, claridad y permitir importación como módulo.

## Patrones y convenciones del código

- Estilo imperativo y procedural: funciones pequeñas, variables globales en `clase1.py`.
- Interacción por `input()` y salida por `print()` — asume un terminal humano.
- Comentarios y nombres en español; mantener ese idioma en PRs y mensajes de commit.

## Flujo de trabajo del desarrollador (comandos útiles)

- Ejecutar ejemplos desde la raíz del repo:

  - `python3 clase1.py`  # ver animación N-reinas en terminal
  - `python3 clase2.py`  # interacción por consola

- Para pruebas rápidas sin interacción (ejemplo):

  - `printf "1234\n1234\n" | python3 clase2.py`  # simula inputs

## Reglas específicas para cambios sugeridos por el agente

1. No eliminar la interacción por defecto. Si añades opciones programáticas (flags o API), hazlo no intrusivo: añadir `if __name__ == "__main__":` y dejar funciones importables.
2. Separar lógica de UI: mover `input()`/`print()`/`clear()` a la sección `__main__` o a funciones `run_*`; la función de lógica debe aceptar y devolver datos (ej.: `solve_n_queens(n, visual=False)` o `clave_candado(passwd, attempt)`).
3. Evitar cambios visuales permanentes: reemplaza `os.system('clear')` y `time.sleep()` por llamadas opcionales controladas con flags (`visual=True`) para facilitar pruebas y CI.
4. Mantener idioma español en mensajes y comentarios a menos que se proponga un cambio de alcance mayor.

## Ejemplos concretos que el agente puede aplicar

- Extraer lógica: en `clase1.py` crear `def solve_n_queens(n: int, visual: bool=False) -> List[List[int]]:` que devuelva soluciones y, sólo si `visual=True`, haga limpieza y dibujado.
- Añadir `if __name__ == "__main__"` que parsea `--no-visual` con `argparse` y llama a la API interna.
- En `clase2.py` mover `input()` bajo `__main__` y exponer `clave_candado(contraseña: str, intento: str) -> bool`.

## Dependencias e integración

- Sólo usa la biblioteca estándar (`time`, `os`). No hay servicios externos ni CI configurada.

## Qué evitar

- Cambios masivos al estilo de los ejercicios (refactors completos) sin pedir confirmación. Este repo es material educativo: aplicar refactors pequeños y reversibles.
- Añadir tests o infra fuera de una carpeta `tests/` sin coordinación.

## Preguntas al autor/maintainer (si se necesita más contexto)

- ¿Deseas que la animación quede desactivada por defecto en PRs orientadas a tests? 
- ¿Prefieres mensajes en inglés para el repo o mantener español?

Por favor, dime si quieres que aplique alguno de los cambios ejemplo (añadir `__main__`, flag `--no-visual`, o extraer la lógica de `clase1.py`).
