from pysnmp.hlapi.v3arch.asyncio import (
    get_cmd,
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity
)
import asyncio

# 1. Sua Lista de IPs
mikrotiks = [
    '192.168.88.1',
    '10.0.0.1',
    '10.0.0.254'
]

# 2. Configurações SNMP
comunnity = 'exemplo'  # Substitua pela comunidade SNMP correta
oid_versao = '1.3.6.1.4.1.14988.1.1.4.4.0'


async def consultar_mikrotik(c, ip):
    print(f'[{c + 1}/{len(mikrotiks)}] Consultando IP: {ip} ...')

    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        SnmpEngine(),
        CommunityData(comunnity, mpModel=1),
        await UdpTransportTarget.create((ip, 161), timeout=2, retries=0),
        ContextData(),
        ObjectType(ObjectIdentity(oid_versao))
    )

    if errorIndication:
        print(f'   └── TIMEOUT/FALHA: {errorIndication}')
    elif errorStatus:
        print(f'   └── ERRO SNMP: {errorStatus.prettyPrint()}')
    else:
        for varBind in varBinds:
            print(f'   └── SUCESSO: {varBind[1]}')


async def main():
    print('--- INICIANDO CONSULTA DE VERSÕES MIKROTIK (WINDOWS / PYSNMP 7) ---')
    for c, ip in enumerate(mikrotiks):
        await consultar_mikrotik(c, ip)
    print('--- FIM BAZZINGA ---')

# Roda o laço assíncrono
asyncio.run(main())
