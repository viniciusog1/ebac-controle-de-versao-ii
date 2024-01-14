import seaborn as sns
import pandas as pd

df = pd.read_csv('gasolina.csv')
# código de geração do gráfico e exportação da imagem
sns.lineplot(data=df, x='dia', y='venda', linewidth=3, color='orange').get_figure().savefig('gasolina.png')