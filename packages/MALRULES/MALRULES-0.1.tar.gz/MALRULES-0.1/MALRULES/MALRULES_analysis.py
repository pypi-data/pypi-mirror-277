# MALRULES/MALRULES_analysis.py

import re
import os

heuristic_rules = {
    "suspicious_api_calls": [
        {"pattern": "CreateRemoteThread", "score": 15, "family": "Trojan"},
        {"pattern": "VirtualAlloc", "score": 15, "family": "RAT"},
        {"pattern": "WriteProcessMemory", "score": 15, "family": "Injector"},
        {"pattern": "LoadLibrary", "score": 10, "family": "Downloader"},
        {"pattern": "GetProcAddress", "score": 10, "family": "Downloader"},
        {"pattern": "OpenProcess", "score": 15, "family": "Injector"},
        {"pattern": "TerminateProcess", "score": 15, "family": "Trojan"},
        {"pattern": "WinHttpOpen", "score": 10, "family": "Downloader"},
        {"pattern": "WinHttpSendRequest", "score": 10, "family": "Downloader"},
        {"pattern": "InternetOpen", "score": 10, "family": "Spyware"},
        {"pattern": "InternetConnect", "score": 10, "family": "Spyware"},
        {"pattern": "DeleteFile", "score": 10, "family": "Wiper"},
        {"pattern": "CopyFile", "score": 10, "family": "Spyware"},
        {"pattern": "MoveFile", "score": 10, "family": "Spyware"},
        {"pattern": "CreateFile", "score": 10, "family": "Spyware"},
        {"pattern": "RegOpenKey", "score": 10, "family": "Spyware"},
        {"pattern": "RegSetValue", "score": 10, "family": "Spyware"},
        {"pattern": "RegCreateKey", "score": 10, "family": "Spyware"},
        {"pattern": "RegDeleteKey", "score": 10, "family": "Wiper"},
        {"pattern": "GetVersionEx", "score": 5, "family": "Generic"},
        {"pattern": "GetSystemInfo", "score": 5, "family": "Spyware"},
        {"pattern": "GetUserName", "score": 5, "family": "Spyware"},
        {"pattern": "GetComputerName", "score": 5, "family": "Spyware"},
        {"pattern": "GetAsyncKeyState", "score": 15, "family": "Keylogger"},
        {"pattern": "SetWindowsHookEx", "score": 15, "family": "Keylogger"},
        {"pattern": "GetForegroundWindow", "score": 15, "family": "Keylogger"},
    ],
    "suspicious_patterns": [
        {"pattern": "PE32", "score": 5, "family": "Generic"},
        {"pattern": "MZ", "score": 5, "family": "Generic"},
        {"pattern": "XOR decryption loop", "score": 20, "family": "Ransomware"},
        {"pattern": "Inline assembly", "score": 20, "family": "Rootkit"},
        {"pattern": "Packed section", "score": 20, "family": "Packer"},
        {"pattern": "Encrypted section", "score": 20, "family": "Crypter"},
        {"pattern": "Hidden file extension", "score": 10, "family": "Stealth"},
        {"pattern": "Obfuscated script", "score": 15, "family": "Obfuscator"},
        {"pattern": "Suspicious registry entry", "score": 15, "family": "Spyware"},
        {"pattern": "VM detection", "score": 10, "family": "Anti-VM"},
        {"pattern": "Unusual file size", "score": 10, "family": "Packer"},
        {"pattern": "Suspicious network traffic", "score": 20, "family": "Backdoor"},
        {"pattern": "Command and control communication", "score": 25, "family": "Backdoor"},
        {"pattern": "Scheduled task creation", "score": 15, "family": "Persistence"},
        {"pattern": "Service creation", "score": 15, "family": "Persistence"},
        {"pattern": "File dropping behavior", "score": 20, "family": "Dropper"},
        {"pattern": "Keylogging behavior", "score": 25, "family": "Keylogger"},
        {"pattern": "Persistence mechanism", "score": 20, "family": "Trojan"},
        {"pattern": "Code injection", "score": 30, "family": "Injector"},
        {"pattern": "Code execution from memory", "score": 30, "family": "RAT"},
        {"pattern": "Attempt to disable security software", "score": 30, "family": "Ransomware"},
        {"pattern": "Sandbox evasion", "score": 15, "family": "Anti-VM"},
        {"pattern": "Anomalous API usage", "score": 10, "family": "Generic"},
        {"pattern": "Self-modifying code", "score": 25, "family": "Metamorphic"},
        {"pattern": "Suspicious mutex creation", "score": 10, "family": "Trojan"},
        {"pattern": "Abnormal process behavior", "score": 20, "family": "Rootkit"},
        {"pattern": "Excessive resource usage", "score": 15, "family": "Miner"},
        {"pattern": "Unusual user-agent string", "score": 15, "family": "Spyware"},
        {"pattern": "Suspicious email attachment", "score": 20, "family": "Phishing"},
        {"pattern": "Unusual network port", "score": 10, "family": "Backdoor"},
        {"pattern": "Encrypted payload", "score": 20, "family": "Ransomware"},
        {"pattern": "Suspicious domain name", "score": 20, "family": "Phishing"},
        {"pattern": "Injection into system processes", "score": 30, "family": "Injector"},
        {"pattern": "Tampering with system files", "score": 30, "family": "Wiper"},
        {"pattern": "Anomalous file access", "score": 15, "family": "Spyware"},
    ],
    "suspicious_strings": [
        {"pattern": "cmd.exe /c", "score": 10, "family": "Downloader"},
        {"pattern": "powershell.exe -nop", "score": 10, "family": "Downloader"},
        {"pattern": "eval(", "score": 5, "family": "Obfuscator"},
        {"pattern": "exec(", "score": 5, "family": "Obfuscator"},
        {"pattern": "Base64.decode", "score": 10, "family": "Obfuscator"},
        {"pattern": "XOR", "score": 20, "family": "Crypter"},
        {"pattern": "C:\\Users\\Public\\", "score": 5, "family": "Generic"},
        {"pattern": "C:\\Windows\\System32\\", "score": 5, "family": "Generic"},
        {"pattern": "encrypted_string", "score": 15, "family": "Crypter"},
        {"pattern": "malicious_url.com", "score": 20, "family": "Phishing"},
        {"pattern": "127.0.0.1", "score": 20, "family": "Generic"},
        {"pattern": "hardcoded_ip", "score": 15, "family": "Backdoor"},
        {"pattern": "User-Agent: ", "score": 10, "family": "Spyware"},
        {"pattern": "C2 communication", "score": 20, "family": "Backdoor"},
        {"pattern": "payload URL", "score": 20, "family": "Downloader"},
    ],
    "other_patterns": [
        {"pattern": "suspicious_date", "score": 10, "family": "Generic"},
        {"pattern": "hidden_extension", "score": 10, "family": "Stealth"},
        {"pattern": "large_or_small_size", "score": 10, "family": "Packer"},
        {"pattern": "embedded_script", "score": 15, "family": "Obfuscator"},
        {"pattern": "autorun_entry", "score": 20, "family": "Worm"},
        {"pattern": "network_connection", "score": 25, "family": "Backdoor"},
        {"pattern": "dll_injection", "score": 30, "family": "Injector"},
        {"pattern": "self_replication", "score": 20, "family": "Worm"},
        {"pattern": "string_encryption", "score": 20, "family": "Crypter"},
        {"pattern": "packer_tools", "score": 20, "family": "Packer"},
        {"pattern": "suspicious_import", "score": 10, "family": "Generic"},
        {"pattern": "shellcode", "score": 25, "family": "Exploit"},
        {"pattern": "dropping_files", "score": 20, "family": "Dropper"},
        {"pattern": "keylogging", "score": 25, "family": "Keylogger"},
        {"pattern": "backdoor", "score": 25, "family": "Backdoor"},
        {"pattern": "registry_modification", "score": 20, "family": "Trojan"},
        {"pattern": "execution_from_memory", "score": 30, "family": "RAT"},
        {"pattern": "suspicious_name", "score": 10, "family": "Stealth"},
        {"pattern": "anti_vm", "score": 15, "family": "Anti-VM"},
        {"pattern": "unusual_permissions", "score": 10, "family": "Trojan"},
        {"pattern": "deprecated_api", "score": 5, "family": "Generic"},
        {"pattern": "executable_in_file", "score": 20, "family": "Dropper"},
        {"pattern": "botnet_traffic", "score": 25, "family": "Botnet"},
        {"pattern": "malicious_powershell", "score": 20, "family": "Downloader"},
        {"pattern": "wmi_persistence", "score": 20, "family": "Persistence"},
        {"pattern": "abnormal_process", "score": 20, "family": "Rootkit"},
        {"pattern": "disable_security", "score": 30, "family": "Ransomware"},
        {"pattern": "unusual_context", "score": 10, "family": "Generic"},
        {"pattern": "pe_anomalies", "score": 15, "family": "Packer"},
        {"pattern": "file_access_pattern", "score": 10, "family": "Spyware"},
        {"pattern": "service_creation", "score": 15, "family": "Persistence"},
        {"pattern": "resource_usage", "score": 15, "family": "Miner"},
        {"pattern": "unusual_user_agent", "score": 15, "family": "Spyware"},
        {"pattern": "obfuscated_js", "score": 20, "family": "Obfuscator"},
        {"pattern": "known_vulnerabilities", "score": 25, "family": "Exploit"},
        {"pattern": "sandbox_evasion", "score": 15, "family": "Anti-VM"},
        {"pattern": "scheduled_task", "score": 15, "family": "Persistence"},
        {"pattern": "email_attachment", "score": 20, "family": "Phishing"},
        {"pattern": "network_port", "score": 10, "family": "Backdoor"},
        {"pattern": "malicious_powershell_script", "score": 20, "family": "Downloader"},
        {"pattern": "encrypted_payload", "score": 20, "family": "Ransomware"},
        {"pattern": "suspicious_domain", "score": 20, "family": "Phishing"},
        {"pattern": "system_process_injection", "score": 30, "family": "Injector"},
        {"pattern": "tampering_system_files", "score": 30, "family": "Wiper"},
        {"pattern": "suspicious_mutex", "score": 10, "family": "Trojan"},
        {"pattern": "behavioral_anomalies", "score": 20, "family": "Rootkit"},
    ],
}

def check_suspicious_strings(file_content, rules):
    score = 0
    families = set()
    for rule in rules:
        if re.search(re.escape(rule["pattern"]), file_content):
            score += rule["score"]
            families.add(rule["family"])
    return score, families

def check_suspicious_api_calls(file_content, rules):
    score = 0
    families = set()
    for rule in rules:
        if re.search(re.escape(rule["pattern"]), file_content):
            score += rule["score"]
            families.add(rule["family"])
    return score, families

def check_suspicious_patterns(file_content, rules):
    score = 0
    families = set()
    for rule in rules:
        if re.search(re.escape(rule["pattern"]), file_content):
            score += rule["score"]
            families.add(rule["family"])
    return score, families

def check_other_patterns(file_content, rules):
    score = 0
    families = set()
    for rule in rules:
        if re.search(re.escape(rule["pattern"]), file_content):
            score += rule["score"]
            families.add(rule["family"])
    return score, families

def calculate_suspicion_score_and_families(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        file_content = file.read()

    total_score = 0
    detected_families = set()

    score, families = check_suspicious_strings(file_content, heuristic_rules["suspicious_strings"])
    total_score += score
    detected_families.update(families)

    score, families = check_suspicious_api_calls(file_content, heuristic_rules["suspicious_api_calls"])
    total_score += score
    detected_families.update(families)

    score, families = check_suspicious_patterns(file_content, heuristic_rules["suspicious_patterns"])
    total_score += score
    detected_families.update(families)

    score, families = check_other_patterns(file_content, heuristic_rules["other_patterns"])
    total_score += score
    detected_families.update(families)

    return total_score, detected_families

def determine_suspicion_level(score):
    if score >= 150:
        return "Highly Suspicious"
    elif score >= 100:
        return "Suspicious"
    elif score >= 50:
        return "Potentially Suspicious"
    else:
        return "Not Suspicious"

def is_file_suspicious(file_path, threshold=100):
    suspicion_score, detected_families = calculate_suspicion_score_and_families(file_path)
    suspicion_level = determine_suspicion_level(suspicion_score)
    return suspicion_level, suspicion_score, detected_families
