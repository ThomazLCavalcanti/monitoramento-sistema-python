import os
import platform
import psutil
import time
from datetime import datetime, timedelta

def bytes_para_gb(bytes_valor):
    return round(bytes_valor / (1024 ** 3), 2)

def exibir_informacoes_sistema():
    print("="*40)
    print("🖥️  Monitoramento de Sistema")
    print("="*40)

    # Informações básicas do sistema
    print(f"Sistema operacional: {platform.system()} {platform.release()}")
    print(f"Arquitetura: {platform.machine()}")
    print(f"Hostname: {platform.node()}")
    print(f"CPU: {platform.processor()}")
    
    # Uptime
    tempo_ligado = timedelta(seconds=int(time.time() - psutil.boot_time()))
    print(f"Uptime: {tempo_ligado}")

    # CPU
    uso_cpu = psutil.cpu_percent(interval=1)
    print(f"\nUso de CPU: {uso_cpu}%")

    # RAM
    memoria = psutil.virtual_memory()
    print(f"Uso de RAM: {memoria.percent}% ({bytes_para_gb(memoria.used)}GB de {bytes_para_gb(memoria.total)}GB)")

    # Disco
    disco = psutil.disk_usage('/')
    print(f"Uso de Disco: {disco.percent}% ({bytes_para_gb(disco.used)}GB de {bytes_para_gb(disco.total)}GB)")

    print("="*40)

if __name__ == "__main__":
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa terminal
            exibir_informacoes_sistema()
            time.sleep(5)  # Atualiza a cada 5 segundos
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")
