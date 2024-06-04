from database_mysql_local.generic_mapping import GenericMapping
from email_address_local.email_address import EmailAddressesLocal
from language_remote.lang_code import LangCode
from logger_local.MetaLogger import MetaLogger
from user_context_remote.user_context import UserContext

from .contact_email_addresses_constants import CONTACT_EMAIL_ADDRESSES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT

user_context = UserContext()


class ContactEmailAdressesLocal(GenericMapping, metaclass=MetaLogger,
                                object=CONTACT_EMAIL_ADDRESSES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT):
    def __init__(self, default_lang_code: LangCode = None, is_test_data: bool = False) -> None:

        GenericMapping.__init__(
            self, is_test_data=is_test_data,
            default_schema_name="contact_email_address", default_column_name="contact_email_id",
            default_table_name="contact_email_address_table", default_view_table_name="contact_email_address_view",
            default_entity_name1="contact", default_entity_name2="email_address")
        self.email_addresses_local = EmailAddressesLocal(is_test_data=is_test_data)
        self.default_lang_code = default_lang_code  # TODO: not used

    def insert_contact_and_link_to_email_address(
            self, contact_dict: dict, contact_email_address_str: str) -> int or None:
        """
        Insert contact and link to existing or new email address
        :param contact_dict: contact_dict
        :param contact_email_address_str: contact_email_address_str
        :param contact_id: contact_id
        :return: contact_id
        """
        if not contact_email_address_str:
            # TODO: we can try to look if there's an email address in the database by phone number
            # when contact-phones-local is done
            return
        contact_id = contact_dict.get("contact_id")
        person_id = contact_dict.get("person_id")
        profiles_ids = contact_dict.get("profiles_ids")

        email_address_id = self.email_addresses_local.get_email_address_id_by_email_address_str(
            email_address_str=contact_email_address_str)
        if not email_address_id:
            # Create a new  email address and add it to email_address_table and email_address_ml_table
            self.logger.info("email_address_id is None, creating a new email address and adding it to"
                             " email_address_table and email_address_ml_table")
            first_name = contact_dict.get("first_name")
            last_name = contact_dict.get("last_name")
            title = contact_dict.get("title") or f"{first_name} {last_name}"
            lang_code = LangCode.detect_lang_code_restricted(title)
            email_address_id = self.email_addresses_local.insert(
                email_address_str=contact_email_address_str, lang_code=lang_code, title=title)
            if not email_address_id:
                self.logger.error("email_address_id is None")
                return
            # Link contact to email address
            self.logger.info("Linking contact to email address")
            contact_email_address_id = self.insert_mapping(
                entity_id1=contact_id, entity_id2=email_address_id, ignore_duplicate=True)
        else:
            # check if there is link to existing email address
            self.logger.info("Linking contact to existing email address")
            # TODO contact_email_address_mapping_tupple = 
            mapping_tuple = self.select_multi_mapping_tuple_by_id(
                entity_id1=contact_id, entity_id2=email_address_id)
            if not mapping_tuple:
                # Link contact to existing email address
                self.logger.info("Linking contact to existing email address")
                contact_email_address_id = self.insert_mapping(
                    entity_id1=contact_id, entity_id2=email_address_id, ignore_duplicate=True)
            else:
                self.logger.info("contact is already linked to email address", object={
                    "contact_id": contact_id, "email_address_id": email_address_id, "mapping_tuple": mapping_tuple})
                contact_email_address_id = mapping_tuple[0]
        if contact_email_address_id is not None and person_id is not None:
            self.insert_mapping_if_not_exists(
                schema_name="email_address_person", entity_name1="email_address", entity_name2="person",
                entity_id1=email_address_id, entity_id2=person_id, view_table_name="email_address_person_view")
        if contact_email_address_id is not None and profiles_ids:
            for profile_id in profiles_ids:
                self.insert_mapping_if_not_exists(
                    schema_name="email_address_profile", entity_name1="email_address", entity_name2="profile",
                    entity_id1=email_address_id, entity_id2=profile_id, view_table_name="email_address_profile_view")

        return contact_email_address_id
