import subprocess

# 1. Lista de IPs dos MikroTiks
mikrotiks = [
    '192.168.88.1', '10.0.0.1', '10.0.0.254'
]

# 2. Configurações SNMP
comunnity = 'exemplo'  # Substitua pela comunidade SNMP correta
oid_versao = '1.3.6.1.4.1.14988.1.1.4.4.0'

print('--- INICIANDO CONSULTA DE VERSÕES MIKROTIK (SNMPWALK) ---')

# 3. Laço de consulta
for c, ip in enumerate(mikrotiks):
    print(f'[{c + 1}/{len(mikrotiks)}] Consultando IP: {ip} ...')

    # Monta a chamada para o utilitário do sistema
    comando = ['snmpwalk', '-v2c', '-c', comunnity, ip, oid_versao]

    try:
        resultado = subprocess.run(
            comando, capture_output=True, text=True, timeout=2)

        if resultado.returncode == 0:
            saida = resultado.stdout.strip()
            print(f'   └── SUCESSO: {saida}')
        else:
            print(f'   └── FALHA: Sem resposta SNMP ou comunidade incorreta')

    except subprocess.TimeoutExpired:
        print(f'   └── TIMEOUT: Equipamento não respondeu em 2s')
    except FileNotFoundError:
        print(f'   └── ERRO: O comando "snmpwalk" não está instalado no sistema.')
        print('       Dica: No Linux/Debian/Ubuntu, instale usando: sudo apt install snmp')
        break

print('--- FIM Bazzinga xD ---')
