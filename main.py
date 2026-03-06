import os
import re

STATUS_FOLDERS = ["Archive", "Final", "In-Progress"]

COC = {
    "Chapter 1": {
        "Title": "Institutional & Administrative Commitment",
        "Section": [
            "1.1 Administrative Commitment"
        ]
    },
    "Chapter 2": {
        "Title": "Program Scope and Governance",
        "Section": [
            "2.1 Cancer Committee",
            "2.2 Cancer Liaison Physician",
            "2.3 Cancer Committee Meetings",
            "2.4 Cancer Committee Attendance",
            "2.5 Multidisciplinary Cancer Care Conference",
        ]
    },
    "Chapter 3": {
        "Title": "Facilities and Equipment Resources",
        "Section": [
            "3.1 Facility Accreditation",
            "3.2 Evaluation and Treatment Services"
        ]
    },
    "Chapter 4": {
        "Title": "Personnel and Equipment Resources",
        "Section": [
            "4.1 Physician Credentials",
            "4.2 Oncology Nursing Credentials",
            "4.3 Cancer Registry Staff Credentials",
            "4.4 Genetic Counseling and Risk Assessment",
            "4.5 Palliative Care Services",
            "4.6 Rehabilitation Care Services",
            "4.7 Oncology Nutrition Services",
            "4.8 Survivorship Program"
        ]
    },
    "Chapter 5": {
        "Title": "Patient Care - Expectations and Protocols",
        "Section": [
            "5.1 College of American Pathologists Synoptic Reporting",
            "5.2 Psychosocial Distress Screening",
            "5.3 Sentinel Node Biopsy for Breast Cancer",
            "5.4 Axillary Lymph Node Dissection for Breast Cancer",
            "5.5 Wide Local Excision for Primary Cutaneous Melanoma",
            "5.6 Colon Resection",
            "5.7 Total Mesorectal Excision",
            "5.8 Pulmonary Resection",
            "5.9: Smoking Cessation for Patients with Cancer"
        ]
    },
    "Chapter 6": {
        "Title": "Data Surveillance and Systems",
        "Section": [
            "6.1 Cancer Registry Quality Control",
            "6.4 Rapid Cancer Reporting System: Data Submission",
            "6.5 Follow-Up of Patients"
        ]
    },
    "Chapter 7": {
        "Title": "Quality Improvement",
        "Section": [
            "7.1 Quality Measures",
            "7.2 Monitoring Concordance with Evidence-Based Guidelines",
            "7.3 Quality Improvement Initiative",
            "7.4 Cancer Program Goal"
        ]
    },
    "Chapter 8": {
        "Title": "Education - Professional and Community Outreach",
        "Section": [
            "8.1 Addressing Barriers to Care",
            "8.2 Cancer Prevention Event",
            "8.3 Cancer Screening Event"
        ]
    },
    "Chapter 9": {
        "Title": "Research",
        "Section": [
            "9.1 Clinical Research Accrual",
            "9.2 Commission on Cancer Special Studies"
        ]
    }
}


NAPBC = {
    "Chapter 1": {
        "Title": "Institutional & Administrative Commitment",
        "Section": [
            "1.1 Administrative Commitment"
        ]
    },
    "Chapter 2": {
        "Title": "Program Scope and Governance",
        "Section": [
            "2.1 Breast Program Leadership Committee",
            "2.2 Breast Program Director",
            "2.3 Breast Care Team",
            "2.4 Multidisciplinary Breast Care Conference"
        ]
    },
    "Chapter 3": {
        "Title": "Facilities and Equipment Resources",
        "Section": [
            "3.1 Facility Accreditation",
            "3.2 Radiation Oncology Quality Assurance",
            "3.3 Image Guided Biopsy Quality Assurance",
            "3.4 Breast Imaging Quality Assurance",
            "3.5 Pathology Quality Assurance"
        ]
    },
    "Chapter 4": {
        "Title": "Personnel and Equipment Resources",
        "Section": [
            "4.1 Physician Credentials",
            "4.2 Oncology Nursing Credentials",
            "4.3 Physician Assistant Credentials",
            "4.4 Genetic Professional Credentials",
            "4.5 Patient Navigator Credentials"
        ]
    },
    "Chapter 5": {
        "Title": "Patient Care- Expectations and Protocols",
        "Section": [
            "5.1 Screening for Breast Cancer",
            "5.2 Diagnostic Imaging of the Breast and Axilla",
            "5.3 Evaluation and Management of Benign Breast Diseases",
            "5.4 Management of Patients at Increased Risk for Breast Cancer",
            "5.5 Genetic Evaluation and Management",
            "5.6 Evaluation and Treatment Planning for the Newly Diagnosed Cancer Patient",
            "5.7 Comprehensive Evaluation of Patient Factors Before Treatment",
            "5.8 Patient Navigation",
            "5.9 Surgical Care",
            "5.10 Reconstructive Surgery",
            "5.11 Medical Oncology",
            "5.12 Radiation Oncology",
            "5.13 Surgical Pathology",
            "5.14 Breast Cancer Staging Using the AJCC System",
            "5.15 Survivorship",
            "5.16 Surveillance"
        ]
    },
    "Chapter 7": {
        "Title": "Quality Improvement",
        "Section": [
            "7.1 Quality Measures",
            "7.2 Quality Improvement Initiatives"
        ]
    },
    "Chapter 8": {
        "Title": "Education- Professional and Community Outreach",
        "Section": [
            "8.1 Education, Prevention, and Early Detection Programs",
            "8.2 Continuing Education"
        ]
    },
    "Chapter 9": {
        "Title": "Research",
        "Section": [
            "9.1 Clinical Research Accrual"
        ]
    }
}


def sanitize_folder_name(name: str) -> str:
    """Remove characters that commonly cause problems in folder names."""
    name = name.strip()
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    return name


def make_status_folders(section_path: str) -> None:
    """Create Archive, Final, and In-Progress inside a section folder."""
    for folder in STATUS_FOLDERS:
        os.makedirs(os.path.join(section_path, folder), exist_ok=True)


def get_standard_set() -> tuple[str, dict]:
    """
    Ask user which standards to build and return:
    - top-level folder name
    - corresponding standards dictionary
    """
    choice = input("CoC or NAPBC standards? ").strip().upper()

    if choice == "COC":
        return "CoC", COC
    elif choice == "NAPBC":
        return "NAPBC", NAPBC
    else:
        raise ValueError("Invalid choice. Please enter either 'CoC' or 'NAPBC'.")


def create_accreditation_structure(base_path: str, standard_name: str, chapters: dict) -> None:
    """Create full folder structure for the selected accreditation program."""
    standard_root = os.path.join(base_path, standard_name)
    os.makedirs(standard_root, exist_ok=True)

    for chapter, chapter_data in chapters.items():
        title = sanitize_folder_name(chapter_data["Title"])
        sections = chapter_data["Section"]

        chapter_folder_name = sanitize_folder_name(f"{chapter} {title}")
        chapter_path = os.path.join(standard_root, chapter_folder_name)
        os.makedirs(chapter_path, exist_ok=True)

        print(chapter_folder_name)

        for section in sections:
            section_folder_name = sanitize_folder_name(section)
            section_path = os.path.join(chapter_path, section_folder_name)

            os.makedirs(section_path, exist_ok=True)
            make_status_folders(section_path)

            print(f"  {section_folder_name}")


def main() -> None:
    current_directory = os.getcwd()

    try:
        standard_name, chapter_dict = get_standard_set()
        create_accreditation_structure(current_directory, standard_name, chapter_dict)
        print(f"\nFolder structure created successfully for {standard_name}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
