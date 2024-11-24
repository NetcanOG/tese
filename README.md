## Pasta da tese "Advancements in Vertical Federated Learning: Efficient Learning with Lightweight Models"

Contém bastante lixo de várias experiências, algum que já foi removido, muito que não. Este readme vai focar no estritamente necessário para correr os mesmos exemplos que os da tese.

### Datasets

Os datasets utilizados estão todos organizados na pasta "datasets", com a versão 2, 3, e small para cada dataset, sendo a "small" a versão completa do dataset original com o trimming necessário, e as versões 2 e 3 sendo versões recortadas do "small" com a divisão de features feita para os testes do NVFlare com 2 ou 3 participantes (a versão small é utilizada para 5 participantes). Estes estão prontos para utilizar no NVFlare.

### Versões

Python 3.10, versões de packages em "requirements.txt", recomendado o uso de um environment. A versão do NVFlare é a 2.4. A pasta "vertical_xgboost_thesis" deve ser inserida no repo da NVFlare em examples/advanced/.

### Como correr testes locais

Os testes locais para cada dataset estão na pasta kaggle/(dataset), e os testes são corridos com o xgb_local.py . No mesmo ficheiro estão as versões diferentes do dataset, como na pasta "datasets". No entanto, antes de correr algum teste local, deve-se primeiro correr o "vertical_trim.py" com o dataset pretendido. Isto vai criar um "(dataset)_vertical_trim.csv", que vai ser uma versão recortada do dataset original que vai corresponder à interseção gerada no NVFlare para imitar um sistema VFL. 

### Como correr testes federados

Os testes são corridos na pasta "2.4/NVFlare/examples/advanced/vertical_xgboost_thesis". Para alterar o dataset e configurar as propriedades do teste, como número de clientes, interseção, etc, do NVFlare, alterar os valores no "prepare_data.sh". Para alterar os parâmetros do XGBoost dentro do NVFlare, ver "jobs/app/config". Para correr os testes, seguir os passos descritos no readme.
