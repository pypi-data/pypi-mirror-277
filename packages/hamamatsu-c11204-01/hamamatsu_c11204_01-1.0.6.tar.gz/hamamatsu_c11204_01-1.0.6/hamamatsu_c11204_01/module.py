def number_to_ascii(number):
    # Keep the first 8 bits
    first_8_bits = number & 0xFF
    
    # Split the first 8 bits into two nibbles
    nibble1 = first_8_bits >> 4
    nibble2 = first_8_bits & 0x0F
    
    # Convert each nibble to its ASCII representation
    ascii_nibble1 = nibble1 + ord('0') if nibble1 < 10 else nibble1 - 10 + ord('A')
    ascii_nibble2 = nibble2 + ord('0') if nibble2 < 10 else nibble2 - 10 + ord('A')
    
    return ascii_nibble1, ascii_nibble2

def command_to_hex(command, *argv):
    STX = 0x02
    ETX = 0x03
    CR = 0x0D

    hex_STX = f"0x{STX:02X}"
    hex_ETX = f"0x{ETX:02X}"
    hex_CR = f"0x{CR:02X}"

    hex_command = [f"0x{ord(c):02X}" for c in command]

    # Dictionary that associates each command with the expected number of parameters
    command_parameters = {
        'HPO': 0, 'HST': 6, 'HRT': 0, 'HOF': 0, 'HON': 0, 'HCM': 1,
        'HRE': 0, 'HBV': 1, 'HGT': 0, 'HGV': 0, 'HGC': 0, 'HGS': 0
    }

    if command not in command_parameters:
        raise ValueError(f"Command '{command}' not recognized.")

    if len(argv) != command_parameters[command]:
        raise ValueError(f"The command '{command}' requires exactly {command_parameters[command]} parameters, received {len(argv)}.")

    # Convert all parameters to integers
    parameters = [int(p) for p in argv]

    hex_parameters = []
    for p in parameters:
        if command == 'HST' or command == 'HBV':
            hex_param = f"{p:04X}"
        elif command == 'HCM':
            hex_param = f"{p:01X}"
        else:
            hex_param = f"{p:04X}"
        # Split hex_param into individual characters and convert them to ASCII
        for char in hex_param:
            ascii_value = f"0x{ord(char):02X}"
            hex_parameters.append(ascii_value)

    # Calculate the checksum value
    checksum_val = (
        STX + 
        sum(ord(c) for c in command) + 
        sum(int(hex_parameters[i], 16) for i in range(len(hex_parameters))) + 
        ETX
    )
    checksum_val %= 256

    # Split the checksum value into two ASCII nibbles
    nibble1, nibble2 = number_to_ascii(checksum_val)
    
    result = [hex_STX] + hex_command + hex_parameters + [hex_ETX, f"0x{nibble1:02X}", f"0x{nibble2:02X}", hex_CR]

    return result

def send_command(command, *argv):
    hex_string = command_to_hex(command, *argv)
    for hex_value in hex_string:
        send_hex(ser, hex_value)

def send_hex(fd, hex_value):
    value = int(hex_value, 16)
    print(value)
    ser.write(value.to_bytes(1, byteorder='big'))  # alternatively, could be 'little'
    print(f"Sending: {hex_value}")

def read_from_source():
    data = ser.read(32)
    ascii_data = data.decode('ascii', errors='ignore')
    return ascii_data


dict_conv = {
    'out_volt_mon': 1.812e-3,
    'out_corr_mon': 4.980e-3,
    'MPPC_temp_mon': 1.907e-5/-5.5e-3,
    'sec_high_temp': 1.507e-3,
    'sec_low_temp': 1.507e-3,
    'prim_high_temp': 5.225e-2,
    'prim_low_temp': 5.225e-2,
    'volt_ref': 1.812e-3,
    'temp_ref': 1.907e-5/-5.5e-3
}

error_dict = {
    "0001": "UART communication error",
    "0002": "Timeout error",
    "0003": "Syntax error",
    "0004": "Checksum error",
    "0005": "Command error",
    "0006": "Parameter error",
    "0007": "Parameter size error"
}

def error_codes(lect):
  error_dict = {
    "0001": "UART communication error",
    "0002": "Timeout error",
    "0003": "Syntax error",
    "0004": "Checksum error",
    "0005": "Command error",
    "0006": "Parameter error",
    "0007": "Parameter size error"}
  error_no = lect.split('hxx')[-1].split('\x03')[0]
  return error_dict.get(error_no)

def hex_to_dec(hexa):
    return int(hexa, 16)

def status_dict(hex_string):
  if len(hex_string)>4:
    return 'Error: Hex value longer than 4 bytes.'
  else:
    hex_to_bin = bin(int(hex_string, 16))[2:].zfill(8)
    hvo_status_b = str(hex_to_bin)[-1]
    over_curr_status_b = str(hex_to_bin)[-2]
    curr_value_status_b = str(hex_to_bin)[-3]
    mppc_temp_sensor_status_3_b = str(hex_to_bin)[-4]
    mppc_temp_sensor_status_4_b = str(hex_to_bin)[-5]
    temp_corr_status_b = str(hex_to_bin)[-7]
    if hvo_status_b=='1':
      hvo_status = 'ON'
    else:
      hvo_status = 'OFF'
    if over_curr_status_b=='1':
      over_curr_status = 'Yes'
    else:
      over_curr_status = 'No'
    if curr_value_status_b=='1':
      curr_value_status = 'Outside specifications'
    else:
      curr_value_status = 'Within specifications'
    if mppc_temp_sensor_status_3_b=='1':
      mppc_temp_sensor_status_3 = 'Connect'
    else:
      mppc_temp_sensor_status_3 = 'Disconnect'
    if mppc_temp_sensor_status_4_b=='1':
      mppc_temp_sensor_status_4 = 'Outside specifications'
    else:
      mppc_temp_sensor_status_4 = 'Within specifications'
    if temp_corr_status_b=='1':
      temp_corr_status = 'Effectiveness'
    else:
      temp_corr_status = 'Invalid'

    return {'hvo_status': hvo_status, 'over_curr_status': over_curr_status, 'curr_value_status': curr_value_status,
          'mppc_temp_sensor_status_3': mppc_temp_sensor_status_3, 'mppc_temp_sensor_status_4': mppc_temp_sensor_status_4,
          'temp_corr_status': temp_corr_status}

def poling():
    send_command('HPO')
    reading = read_from_source()
    lect_pol = reading.split('hpo')[-1].split('\x03')[0]
    list_coefs = [lect_pol[i:i+4] for i in range(0, len(lect_pol), 4)]
    status = status_dict(list_coefs[0])
    out_volt_sett = list_coefs[1]
    out_volt_mon = list_coefs[2]
    out_curr_mon = list_coefs[3]
    MPPC_temp_mon = list_coefs[4]
    if 'hpo' in reading:
        out_volt_sett_f = int(out_volt_sett, 16) * dict_conv['volt_ref']
        out_volt_mon_f = int(out_volt_mon, 16) * dict_conv['out_volt_mon']
        out_curr_mon_f = int(out_curr_mon, 16) * dict_conv['out_curr_mon']
        
        if status['mppc_temp_sensor_status_3'] == 'Disconnect' or MPPC_temp_mon == '7C18':
            MPPC_temp_mon_f = 'Sensor disconnected'
        else:
            MPPC_temp_mon_f = int(MPPC_temp_mon, 16) * dict_conv['MPPC_temp_mon']
        return status, out_volt_sett_f, out_volt_mon_f, out_curr_mon_f, MPPC_temp_mon_f
    else:
        return f'Error: {error_codes(reading)}.'

def set_temperature_factor(secondary_coefs_high, secondary_coefs_low, primary_coefs_high, primary_coefs_low, ref_volt, ref_temp):
    # Create a function that converts the coefficient values passed to the function to hex
    send_command('HST', sch=secondary_coefs_high, scl=secondary_coefs_low, ph=primary_coefs_high, pl=primary_coefs_low, rv=ref_volt, rt=ref_temp)
    reading = read_from_source()
    temp_factor = reading.split('HST')[-1].split('\x03')[0]
    if 'hcm' in reading:
        return temp_factor
    else:
        return f'Error: {error_codes(reading)}.'

def read_temperature_factor():
    send_command('HRT')
    reading = read_from_source()
    coefs = reading.split('\x03')[0].split('hrt')[-1]
    list_coefs = [coefs[i:i+4] for i in range(0, len(coefs), 4)]
    secondary_coefs_high = list_coefs[0]
    secondary_coefs_low = list_coefs[1]
    primary_coefs_high = list_coefs[2]
    primary_coefs_low = list_coefs[3]
    ref_volt = list_coefs[4]
    ref_temp = list_coefs[5]
    if 'hrt' in reading:
        return secondary_coefs_high, secondary_coefs_low, primary_coefs_high, primary_coefs_low, ref_volt, ref_temp
    else:
        return f'Error: {error_codes(reading)}.'


def turn_on():
    send_command('HON')
    reading = read_from_source()
    output_voltage = reading.split('hon')[-1].split('\x03')[0]
    if 'hon' in reading:
        return output_voltage
    else:
        return f'Error: {error_codes(reading)}.'


def turn_off():
    send_command('HOF')
    reading = read_from_source()
    output = reading.split('hof')[-1].split('\x03')[0]
    if output == '':
        return "Power turned off."
    else:
        return f'Error: {error_codes(reading)}.'

def switch_tcm(mode):
    send_command('HCM', mode=mode)
    reading = read_from_source()
    output = reading.split('hcm')[-1].split('\x03')[0]
    if 'hcm' in reading:
        return output
    else:
        return f'Error: {error_codes(reading)}.'

def reset_ps():
    send_command('HRE')
    reading = read_from_source()
    output = reading.split('hre')[-1].split('\x03')[0]
    if 'hre' in reading:
        return output
    else:
        return f'Error: {error_codes(reading)}.'


def set_volt_ref(v_ref):
    '''Temporarily sets the power supply voltage. The setting is lost when turned off.'''
    if (v_ref < 50) or (v_ref > 90):
        return 'Reference voltage out of operating limits.'
    else:
        v_ref_int = int(v_ref / 1.812e-3)
        send_command('HBV', v_ref_int)
        reading = read_from_source()
        set_voltage = reading.split('hbv')[-1].split('\x03')[0]
        if 'hbv' in reading:
            return f'Successfully set reference voltage to {v_ref_int * 1.812e-3}V.'
        else:
            return f'Error: {error_codes(reading)}.'


def get_temp_aq_mppc():
    send_command('HGT')
    reading = read_from_source()
    temp_mppc = reading.split('hgt')[-1].split('\x03')[0]
    if 'hgt' in reading:
        dec = hex_to_dec(temp_mppc)
        float_temp = dec * dict_conv['MPPC_temp_mon']
        return f'MPPC Temperature: {float_temp}°C'
    else:
        return f'Error: {error_codes(reading)}.'

def get_voltage():
    send_command('HGV')
    reading = read_from_source()
    output_voltage = reading.split('hgv')[-1].split('\x03')[0]
    if 'hgv' in reading:
        dec = hex_to_dec(output_voltage)
        float_voltage = dec * dict_conv['out_volt_mon']
        return float_voltage
    else:
        return f'Error: {error_codes(reading)}.'

def get_current():
    send_command('HGC')
    reading = read_from_source()
    output_current = reading.split('hgc')[-1].split('\x03')[0]
    if 'hgc' in reading:
        dec = hex_to_dec(output_current)
        float_current = dec * dict_conv['out_volt_mon']
        return float_current
    else:
        return f'Error: {error_codes(reading)}.'
