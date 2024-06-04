from itertools import chain
from unittest import TestCase

from content_security_policy.constants import KEYWORD_SOURCES, NONE
from content_security_policy.parse import _PARSING_RULES
from content_security_policy.utils import kebab_to_snake
from content_security_policy.values import KeywordSource, NoneSrc


class ValueCompleteness(TestCase):
    def test_all_values_have_pattern(self):
        for value_type in chain(*_PARSING_RULES.values()):
            self.assertTrue(hasattr(value_type, "pattern"))


class KeywordSourceAttributes(TestCase):
    def test_keyword_source_attributes(self):
        for kw_src in KEYWORD_SOURCES:
            with self.subTest(kw_src):
                attr_name = kebab_to_snake(kw_src).strip("'")
                if not hasattr(KeywordSource, attr_name):
                    self.fail(f"{KeywordSource.__name__} has no attribute {attr_name}")
                elif not isinstance(getattr(KeywordSource, attr_name), KeywordSource):
                    self.fail(
                        f"{KeywordSource.__name__}.{attr_name} is not an instance of {KeywordSource}"
                    )
                else:
                    self.assertEqual(kw_src, str(getattr(KeywordSource, attr_name)))


class NoneSourceStr(TestCase):
    def test_instance_str(self):
        self.assertEqual(NONE, str(NoneSrc()))

    def test_class_str(self):
        self.assertEqual(NONE, str(NoneSrc))

    def test_value_constructor(self):
        as_str = "'NOnE'"
        instance = NoneSrc(_value=as_str)
        self.assertEqual(as_str, str(instance))
