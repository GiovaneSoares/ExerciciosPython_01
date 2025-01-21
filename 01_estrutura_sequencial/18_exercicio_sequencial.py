# """Exercício 18.
# Estimativa de Tempo de Download
# Escreva um programa que calcule o tempo estimado necessário para baixar um arquivo,
# considerando o tamanho do arquivo em megabytes (MB) e a velocidade da conexão de
# internet em megabits por segundo (Mbps).
# Calcule o tempo necessário para o download do arquivo e apresente-o ao usuário em
# minutos.
# Lembrete:
#     1 byte = 8 bits
# Fórmula:
#  Tempo (s) = Tamanho do Arquivo (MB) * 8 / Velocidade da Conexão (Mbps)

tamanho_arquivo_mb = float(input("Tamanho do arquivo (em MB): "))

velocidade_internet_mbps = float(input("Velocidade da conexão da internet (em MBPS): "))

velocidade_internet_mb_segundo = velocidade_internet_mbps / 8

tempo_download_segundo = tamanho_arquivo_mb / velocidade_internet_mb_segundo

tempo_download_minuto = tempo_download_segundo / 60

print(f"Tempo estimado de download: {tempo_download_minuto:.2f} minutos.")
