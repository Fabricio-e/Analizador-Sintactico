Propósito del Sistema

Este sistema está diseñado para procesar y validar expresiones en un lenguaje simplificado mediante dos etapas fundamentales:

Procesamiento Léxico: Transforma el texto de entrada en una secuencia de componentes léxicos (tokens) identificables, como valores numéricos, operadores matemáticos, símbolos de agrupación y, opcionalmente, estructuras de control.

Validación Sintáctica: Evalúa si la secuencia de tokens generada cumple con las reglas gramaticales establecidas. Si es válida, construye una representación jerárquica del código (árbol de sintaxis abstracta o AST) en forma de estructuras anidadas. En caso contrario, notifica errores de sintaxis.

Guía de Uso
Requisitos Previos

Python instalado en el sistema.

Módulo ply disponible (instalable mediante pip install ply).

Pasos para la Ejecución

Preparación de Archivos

Almacena el analizador léxico en un archivo denominado lexer.py.

Guarda el analizador sintáctico en parser.py, ubicado en la misma carpeta que el anterior.

Ejecución del Sistema

Abre una terminal y navega hasta el directorio que contiene los archivos.

Ejecuta el analizador sintáctico con el comando:

bash
python parser.py  
El script cargará automáticamente el lexer desde lexer.py y procesará las expresiones de prueba definidas en su bloque principal (if __name__ == '__main__':).

Interpretación de Resultados

Si la entrada es válida, se mostrará el AST generado.

En caso de errores (símbolos inválidos o estructura incorrecta), se indicará el problema detectado.

Casos de Prueba
Ejemplo 1: Operación Básica

Entrada: 5 * 3

Salida: ('*', ('NUM', 5), ('NUM', 3))
El sistema identifica la multiplicación y representa los operandos como tokens numéricos.

Ejemplo 2: Expresión Compleja con Prioridad

Entrada: (8 + 2) / 2

Salida: ('/', ('+', ('NUM', 8), ('NUM', 2)), ('NUM', 2))
Los paréntesis modifican la precedencia estándar, agrupando primero la suma antes que la división.

Ejemplo 3: Uso de Palabras Clave (Opcional)

Entrada: if x + 1

Salida: Tokenización de if como palabra reservada, seguida de la expresión x + 1 (asumiendo que x es un identificador válido).

Notas Adicionales

El sistema ignora espacios y tabulaciones durante el análisis.

Los errores léxicos (como caracteres no permitidos) se señalan sin interrumpir el procesamiento del resto de la entrada.

La estructura del AST puede adaptarse para soportar más operadores o reglas gramaticales según necesidades futuras.
