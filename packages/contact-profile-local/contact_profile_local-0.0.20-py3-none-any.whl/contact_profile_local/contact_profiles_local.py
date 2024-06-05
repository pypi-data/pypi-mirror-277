from contact_persons_local.contact_persons_local import ContactPersonsLocal
from database_mysql_local.generic_mapping import GenericMapping
from language_remote.lang_code import LangCode
from logger_local.MetaLogger import MetaLogger
from profile_local.profiles_local import ProfilesLocal
from user_context_remote.user_context import UserContext

from .contact_profiles_local_constants import CONTACT_PROFILES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT

DEFAULT_SCHEMA_NAME = "contact_profile"
DEFAULT_ENTITY_NAME1 = "contact"
DEFAULT_ENTITY_NAME2 = "profile"
DEFAULT_ID_COLUMN_NAME = "contact_profile_id"
DEFAULT_TABLE_NAME = "contact_profile_table"
DEFAULT_VIEW_TABLE_NAME = "contact_profile_view"

user_context = UserContext()


class ContactProfilesLocal(GenericMapping, metaclass=MetaLogger,
                           object=CONTACT_PROFILES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT):
    """Class to manage many ContactProfile Objects."""

    def __init__(self, lang_code: LangCode = None, is_test_data: bool = False) -> None:

        GenericMapping.__init__(self, default_schema_name=DEFAULT_SCHEMA_NAME,
                                default_entity_name1=DEFAULT_ENTITY_NAME1,
                                default_entity_name2=DEFAULT_ENTITY_NAME2,
                                default_column_name=DEFAULT_ID_COLUMN_NAME,
                                default_table_name=DEFAULT_TABLE_NAME,
                                default_view_table_name=DEFAULT_VIEW_TABLE_NAME,
                                is_test_data=is_test_data)
        self.profiles_local = ProfilesLocal(is_test_data=is_test_data)
        self.contact_persons_local = ContactPersonsLocal(is_test_data=is_test_data)
        # TODO: I think we can delete the following line and lang_code parameter
        self.lang_code = lang_code or user_context.get_effective_profile_preferred_lang_code()

    def insert_and_link_contact_profile(self, *, contact_dict: dict, contact_id: int = None,
                                        person_id: int = None, visibility_id: int = 0,
                                        is_approved: bool = True, stars: int = 0,
                                        last_dialog_workflow_state_id: int = 1) -> dict:
        """Insert contact and link to existing or new email address"""
        # We prefer to get contact_id from contact_dict, but for backward compatibility we also accept contact_id argument
        contact_id = contact_dict.get("contact_id") or contact_id
        # We prefer to get person_id from contact_dict, but for backward compatibility we also accept person_id argument
        person_id = contact_dict.get("person_id") or person_id
        person_ids = self.contact_persons_local.get_person_ids_by_contact_id(
            contact_id=contact_id,
            limit=1,
            order_by="contact_person_id DESC"
        )
        profiles_ids_list = []
        contact_profiles_ids_list = []
        if person_id is not None and person_id not in person_ids:
            person_ids.insert(0, person_id)
        if person_ids:
            person_id = person_ids[0]
            # TODO profile_ids_of_a_person_tuple_list
            profile_ids_tuples_list = self.profiles_local.select_multi_tuple_by_column_and_value(
                select_clause_value="profile_id",
                column_name="main_person_id",
                column_value=person_id
            )
            if not profile_ids_tuples_list:
                # Create a new  profile and add it to profile_table and profile_ml_table
                self.logger.info("profile_id is None, creating a new profile and adding it to"
                                 " profile_table and profile_ml_table")
                lang_code_str = LangCode.detect_lang_code_str_restricted(
                    text=contact_dict.get("display_as"), default_lang_code=LangCode.ENGLISH.value)
                profile_dict = {
                    "main_person_id": person_id,
                    "name": contact_dict.get("display_as"),
                    "lang_code": lang_code_str,
                    "visibility_id": visibility_id,
                    "is_approved": is_approved,
                    "is_main": True,
                    "stars": stars,
                    "last_dialog_workflow_state_id": last_dialog_workflow_state_id
                }
                profile_id = self.profiles_local.insert(
                    main_person_id=person_id, profile_dict=profile_dict)
                if profile_id is None:
                    self.logger.error(
                        "profile was not created and inserted to the database, profile_id is None")
                    return {}
                else:
                    self.logger.info("profile was created and inserted to the database", object={"profile_id": profile_id})
                    profiles_ids_list.append(profile_id)

                self.logger.info("profile was created and inserted to the database")
                self.logger.info("Linking contact to profile")
                contact_profile_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                         entity_name2=self.default_entity_name2,
                                                         entity_id1=contact_id, entity_id2=profile_id)
                if contact_profile_id is None:
                    self.logger.error(
                        "contact was not linked to profile, contact_profile_id is None")
                    return {}
                self.logger.info("contact was linked to profile")
                contact_profiles_ids_list.append(contact_profile_id)
            else:
                for profile_id_tuple in profile_ids_tuples_list:
                    # Check if there is link to existing profile
                    self.logger.info("Checking if there is link to existing profile")
                    profile_id = profile_id_tuple[0]
                    mapping_tuple_list = self.select_multi_mapping_tuple_by_id(
                        entity_name1=self.default_entity_name1, entity_name2=self.default_entity_name2,
                        entity_id1=contact_id, entity_id2=profile_id)
                    if not mapping_tuple_list:
                        # Link contact to existing profile
                        self.logger.info("Linking contact to existing profile")
                        contact_profile_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                                 entity_name2=self.default_entity_name2,
                                                                 entity_id1=contact_id, entity_id2=profile_id)
                    else:
                        self.logger.info("contact is already linked to profile")
                        contact_profile_id = mapping_tuple_list[0][0]
                    profiles_ids_list.append(profile_id)
                    contact_profiles_ids_list.append(contact_profile_id)
            insert_information = {
                "contact_profiles_ids_list": contact_profiles_ids_list,
                "contact_id": contact_id,
                "profiles_ids_list": profiles_ids_list
            }
            return insert_information
