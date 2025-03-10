import pandas as pd

# Criar o DataFrame com os dados fornecidos
dados = {
    'Data': ['15/01/2025'] * 5,
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Temperatura Máxima (°C)': [30.5, 35.0, 24.0, 28.0, 31.0],
    'Temperatura Mínima (°C)': [22.0, 25.0, 18.0, 20.0, 24.5],
    'Precipitação (mm)': [12.0, None, 8.0, 15.0, None],
    'Umidade Relativa (%)': [78, 70, None, 82, 80]
}

df = pd.DataFrame(dados)

# Substituir valores ausentes em Precipitação pela média
df['Precipitação (mm)'].fillna(df['Precipitação (mm)'].mean(), inplace=True)

# Substituir valores ausentes em Umidade Relativa pela mediana
df['Umidade Relativa (%)'].fillna(df['Umidade Relativa (%)'].median(), inplace=True)

# Adicionar coluna Amplitude Térmica
df['Amplitude Térmica'] = df['Temperatura Máxima (°C)'] - df['Temperatura Mínima (°C)']

# Criar novo DataFrame com cidades cuja Temperatura Máxima > 30°C
df_acima_30 = df[df['Temperatura Máxima (°C)'] > 30].copy()

# Reordenar as colunas
colunas_ordenadas = ['Data', 'Cidade', 'Temperatura Máxima (°C)', 'Temperatura Mínima (°C)', 
                     'Amplitude Térmica', 'Precipitação (mm)', 'Umidade Relativa (%)']
df_acima_30 = df_acima_30[colunas_ordenadas]

# Exibir resultado
print("DataFrame filtrado e ajustado (Temperatura Máxima > 30°C):")
print(df_acima_30)