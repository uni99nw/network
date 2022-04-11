import netmiko
import json
import pandas as pd

# 機器情報
device = {
    'device_type':'linux',
    'ip':'x.x.x.x',
    'username':'xxx',
    'password':'xxx',
    'secret':'xxx',
}

# コマンド入力
def ExecCmd(in_cmd):
    with netmiko.ConnectHandler(**device) as con:
        con.enable()
        output = con.send_command(in_cmd)
        con.disable()

    return json.loads(output)


def main():   
    output = ExecCmd('net show system json')
    
    # 必要な情報を定義
    df = {}
    df['vender'] = output['eeprom']['tlv']['Vendor Name']['value']
    df['product'] = output['eeprom']['tlv']['Product Name']['value']
    df['hostname'] = output['hostname']
    df['memory'] = output['memory']
    df['serial'] = output['eeprom']['tlv']['Serial Number']['value']
    df['os-version'] = output['os-version']

    exp_df = pd.DataFrame(list(df.items()), columns=['System info', 'Value'])

    # Export Excel
    exp_df.to_excel('./system_info2.xlsx', index=False)

    # Export CSV
    exp_df.to_csv('./system_info2.csv', index=False)



if __name__ == '__main__':
    main()
