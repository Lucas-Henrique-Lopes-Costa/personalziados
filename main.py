import os
import urllib.parse
import csv

# Definir caminho da pasta de imagens
image_folder_path = 'images'
output_csv = 'franquias.csv'

# Criar ou abrir arquivo CSV para salvar os dados
with open(output_csv, mode='w', newline='') as csvfile:
    fieldnames = ['nome-da-franquia', 'foto-da-franquia', 'link-google-maps', 'tipo']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escrever cabeçalho no CSV
    writer.writeheader()

    # Iterar por todos os arquivos na pasta de imagens
    for image_file in os.listdir(image_folder_path):
        if image_file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Nome da franquia baseado no nome do arquivo (sem extensão)
            franchise_name = os.path.splitext(image_file)[0]

            # Corrigir espaços na URL da imagem
            encoded_image_file = urllib.parse.quote(image_file)
            image_url = f'https://github.com/Lucas-Henrique-Lopes-Costa/personalziados/blob/main/{encoded_image_file}?raw=true'

            # Escrever dados na planilha CSV
            writer.writerow({
                'nome-da-franquia': franchise_name,
                'foto-da-franquia': image_url,
                'link-google-maps': '',
                'tipo': 'pp'
            })

print(f'Dados salvos em {output_csv}')
