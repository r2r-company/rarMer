import requests
import json
import socket
import psutil

def get_system_info():
    hostname = socket.gethostname()
    ip_address = get_ethernet_ip_address()
    memory_info = get_memory_info()
    motherboard_info = get_motherboard_info()
    processor_info = get_processor_info()
    storage_info = get_storage_info()
    free_space_c = get_free_space_c()
    user_id = 1  # Укажите реальный ID пользователя

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "memory_info": memory_info,
        "motherboard_info": motherboard_info,
        "processor_info": processor_info,
        "storage_info": storage_info,
        "free_space_c": free_space_c,
        "user_id": user_id
    }

def get_ethernet_ip_address():
    # Получаем информацию о сетевых интерфейсах
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        if "ethernet" in interface_name.lower():
            for address in interface_addresses:
                if address.family == socket.AF_INET:
                    return address.address
    return None

def get_memory_info():
    # Замените реализацию на получение реальных ID оперативной памяти
    return ["MemoryID1", "MemoryID2"]

def get_motherboard_info():
    # Замените реализацию на получение реальных ID материнской платы
    return ["MotherboardID"]

def get_processor_info():
    # Замените реализацию на получение реальных ID процессора
    return ["ProcessorID"]

def get_storage_info():
    # Замените реализацию на получение реальных ID накопителей
    return ["StorageID1", "StorageID2"]

def get_free_space_c():
    # Замените реализацию на получение реального значения свободного места на диске C
    return 90.5

def send_data(data):
    try:
        response = requests.post("http://127.0.0.1:8000/api/notify/", json=data)
        response.raise_for_status()
        print("Данные успешно отправлены")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке данных: {e}")

if __name__ == "__main__":
    data = get_system_info()
    print(f"Отправка данных: {data}")
    send_data(data)
