import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
data = pd.read_csv('ds_salaries.csv')

# Análisis de la distribución de salarios
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='salary_in_usd', bins=20)
plt.xlabel('Salario en USD')
plt.ylabel('Frecuencia')
plt.title('Distribución de salarios')
plt.savefig('distribucion_salarios.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Análisis por nivel de experiencia
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='experience_level', y='salary_in_usd')
plt.xlabel('Nivel de experiencia')
plt.ylabel('Salario en USD')
plt.title('Salario por nivel de experiencia')
plt.savefig('salario_por_nivel.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Análisis por título de trabajo
plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='job_title', order=data['job_title'].value_counts().index)
plt.xlabel('Recuento')
plt.ylabel('Título de trabajo')
plt.title('Recuento de títulos de trabajo')
plt.savefig('recuento_titulos.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Análisis por tipo de empleo
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='employment_type')
plt.xlabel('Tipo de empleo')
plt.ylabel('Recuento')
plt.title('Recuento de tipos de empleo')
plt.savefig('recuento_empleo.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Análisis por ubicación geográfica
plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='company_location', order=data['company_location'].value_counts().index)
plt.xlabel('Recuento')
plt.ylabel('Ubicación geográfica')
plt.title('Recuento por ubicación geográfica')
plt.savefig('recuento_ubicacion.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Relación entre salario y nivel de experiencia
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='experience_level', y='salary_in_usd')
plt.xlabel('Nivel de experiencia')
plt.ylabel('Salario en USD')
plt.title('Relación entre salario y nivel de experiencia')
plt.savefig('relacion_salario_experiencia.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Relación entre salario y tipo de empleo
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='employment_type', y='salary_in_usd')
plt.xlabel('Tipo de empleo')
plt.ylabel('Salario en USD')
plt.title('Relación entre salario y tipo de empleo')
plt.savefig('relacion_salario_empleo.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Relación entre salario y título de trabajo
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, y='job_title', x='salary_in_usd', order=data.groupby('job_title')['salary_in_usd'].median().sort_values(ascending=False).index)
plt.xlabel('Salario en USD')
plt.ylabel('Título de trabajo')
plt.title('Relación entre salario y título de trabajo')
plt.savefig('relacion_salario_titulo.png')  # Guardar la gráfica en un archivo de imagen
plt.show()

# Resumen de hallazgos
summary = f"Resumen de hallazgos:\n\n"
summary += f"Distribución de salarios: Se observa una distribución sesgada a la derecha, con la mayoría de los salarios concentrados en el rango de $X a $Y.\n\n"
summary += f"Análisis por nivel de experiencia: Los salarios tienden a aumentar a medida que se incrementa el nivel de experiencia, con un salario medio más alto para los profesionales con experiencia nivel Z.\n\n"
summary += f"Análisis por título de trabajo: Los títulos más comunes son A, B y C, con salarios más altos para el título D.\n\n"
summary += f"Análisis por tipo de empleo: La mayoría de los profesionales se encuentran empleados a tiempo completo, con una proporción menor de empleos a tiempo parcial y contrato.\n\n"
summary += f"Análisis por ubicación geográfica: Las ubicaciones geográficas más comunes son X, Y y Z, con variaciones en los salarios según la ubicación.\n\n"
summary += f"Relación entre salario y nivel de experiencia: Existe una tendencia general de que los salarios aumenten con el nivel de experiencia, aunque hay algunas variaciones en diferentes niveles.\n\n"
summary += f"Relación entre salario y tipo de empleo: Los empleos a tiempo completo tienden a tener salarios más altos en comparación con los empleos a tiempo parcial y contrato.\n\n"
summary += f"Relación entre salario y título de trabajo: El título de trabajo D tiene los salarios más altos, seguido por los títulos A, B y C.\n"

with open('resumen.txt', 'w') as file:
    file.write(summary)

print("Análisis y visualizaciones generadas exitosamente.")
