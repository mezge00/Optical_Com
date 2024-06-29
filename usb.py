
import usb.core
import usb.util
import serial
import serial.tools.list_ports

def list_usb_devices():
    devices = usb.core.find(find_all=True)
    for device in devices:
        print(f"Device: ID {device.idVendor:04x}:{device.idProduct:04x}")
        for cfg in device:
            print(f"  Configuration {cfg.bConfigurationValue}")
            for intf in cfg:
                print(f"    Interface {intf.bInterfaceNumber},{intf.bAlternateSetting}")
                for ep in intf:
                    print(f"      Endpoint {ep.bEndpointAddress}")

def list_available_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

def open_serial_port(com_port):
    try:
        print(f"Attempting to open {com_port}...")
        ser = serial.Serial(com_port, baudrate=9600, timeout=1)
        print(f"Successfully opened {com_port}")
        ser.close()
    except serial.SerialException as e:
        print(f"Failed to open {com_port}: {e}")
    except OSError as e:
        print(f"OSError while opening {com_port}: {e}")
    except Exception as e:
        print(f"Unexpected error while opening {com_port}: {e}")

def main():
    print("Listing USB devices:")
    list_usb_devices()
    
    com_port = 'COM7'
    available_ports = list_available_ports()
    print(f"Available ports: {available_ports}")
    
    if com_port not in available_ports:
        print(f"{com_port} is not available. Available ports: {available_ports}")
        return
    
    open_serial_port(com_port)

if __name__ == "__main__":
    main()
