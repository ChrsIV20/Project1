import pandas as pd
import matplotlib.pyplot as plt

# Adatkeret (DataFrame) létrehozása
data = {
    'Tényezők': ['Csoportok között', 'Csoporton belül'],
    'SS': [309.7039683, 1479.866667],
    'df': [83, 1176],
    'MS': [3.731373111, 1.258390023],
    'F': [2.96519604, None],
    'p-érték': [6.94646E-16, None],
    'F krit.': [1.28124675, None]
}
df = pd.DataFrame(data)

# Oszlopdiagram létrehozása
plt.figure(figsize=(8, 6))  # Opcionális: Átméretezés
plt.bar(df['Tényezők'], df['SS'])
plt.ylabel('SS (Squares of Sums)')
plt.title('Egytényezős varianciaanalízis - Oszlopdiagram')

# A diagram megjelenítése
plt.show()
