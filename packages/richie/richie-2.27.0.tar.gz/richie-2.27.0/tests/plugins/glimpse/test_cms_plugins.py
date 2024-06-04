"""
Glimpse plugin tests
"""

from django.db import transaction

from cms.api import add_plugin
from cms.models import Placeholder

from richie.apps.core.factories import PageFactory
from richie.apps.core.tests.utils import CMSPluginTestCase
from richie.plugins.glimpse.cms_plugins import GlimpsePlugin
from richie.plugins.glimpse.factories import GlimpseFactory


# pylint: disable=too-many-ancestors
class GlimpseCMSPluginsTestCase(CMSPluginTestCase):
    """Glimpse plugin tests case"""

    @staticmethod
    @transaction.atomic
    def test_factory_glimpse_title_required():
        """
        The "title" field is not required when instantiating a glimpse.

        Use ``@transaction.atomic`` decorator because of CMSTestCase behavior,
        see details in CMSPluginTestCase docstring.
        """
        GlimpseFactory(title=None)

    @staticmethod
    def test_factory_glimpse_content_not_required():
        """
        The "content" field is not required when instantiating a glimpse.
        """
        GlimpseFactory(content=None)

    def test_factory_glimpse_create_success(self):
        """
        Glimpse plugin creation success
        """
        glimpse = GlimpseFactory(title="Foo")
        self.assertEqual("Foo", glimpse.title)

    def test_models_glimpse_link(self):
        """
        The glimpse model methods "get_link" and "is_blank_target" should
        return the right value depending glimpse has no link, an internal link
        or an external link.
        """
        page = PageFactory(title__title="Internal link")

        glimpse_no_link = GlimpseFactory()
        glimpse_external_link = GlimpseFactory(link_url="http://perdu.com")
        glimpse_internal_link = GlimpseFactory(link_page=page)
        glimpse_both_link = GlimpseFactory(link_url="http://perdu.com", link_page=page)

        # Check expected page url
        self.assertEqual(page.get_absolute_url(), "/en/internal-link/")

        # Check the plugin url
        self.assertEqual(glimpse_no_link.get_link(), None)
        self.assertEqual(glimpse_external_link.get_link(), "http://perdu.com")
        self.assertEqual(glimpse_internal_link.get_link(), page.get_absolute_url())
        self.assertEqual(glimpse_both_link.get_link(), "http://perdu.com")

        # Check the link target
        self.assertEqual(glimpse_no_link.is_blank_target(), False)
        self.assertEqual(glimpse_external_link.is_blank_target(), True)
        self.assertEqual(glimpse_internal_link.is_blank_target(), False)
        self.assertEqual(glimpse_both_link.is_blank_target(), True)

    def test_cms_plugins_glimpse_context_and_html(self):
        """
        Instanciating this plugin with an instance should populate the context
        and render in the template.
        """
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory
        glimpse = GlimpseFactory()

        model_instance = add_plugin(
            placeholder, GlimpsePlugin, "en", title=glimpse.title
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        plugin_context = plugin_instance.render({}, model_instance, None)

        # Check if "instance" is in plugin context
        self.assertIn("instance", plugin_context)

        # Check if parameters, generated by the factory, are correctly set in
        # "instance" of plugin context
        self.assertEqual(plugin_context["instance"].title, glimpse.title)

        # Template context
        context = self.get_practical_plugin_context()

        # Get generated html for glimpse title
        html = context["cms_content_renderer"].render_plugin(model_instance, {})

        # Check rendered title
        self.assertIn(glimpse.title, html)

    def test_cms_plugins_glimpse_header_level(self):
        """
        Header level can be changed from context variable 'header_level'.
        """
        # We deliberately use level '10' since it can be substituted from any
        # reasonable default level.
        header_format = """<h10 class="glimpse-card_square__title">{}</h10>"""

        # Dummy slot where to include plugin
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory
        glimpse = GlimpseFactory()

        # Template context with additional variable to define a custom header
        # level for header markup
        context = self.get_practical_plugin_context({"header_level": 10})

        # Init base Glimpse plugin with required title
        add_plugin(placeholder, GlimpsePlugin, "en", title=glimpse.title)

        # Render placeholder so plugin is fully rendered in real situation
        html = context["cms_content_renderer"].render_placeholder(
            placeholder, context=context, language="en"
        )

        expected_header = header_format.format(glimpse.title)

        # Expected header markup should match given 'header_level' context
        # variable
        self.assertInHTML(expected_header, html)

    def test_cms_plugins_glimpse_compute_variant_default(self):
        """
        When there is no "variant" value set from template parent, if instance
        variant is empty, the variant should default to "square_card".
        """
        placeholder = Placeholder.objects.create(slot="test")

        # Create plugin without a variant
        glimpse_neutral = GlimpseFactory(variant=None)
        model_instance = add_plugin(
            placeholder,
            GlimpsePlugin,
            "en",
            title=glimpse_neutral.title,
            variant=glimpse_neutral.variant,
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        computed_variant = plugin_instance.compute_variant({}, glimpse_neutral)
        self.assertEqual(computed_variant, "card_square")

    def test_cms_plugins_glimpse_compute_variant_without_context_value(self):
        """
        If instance variant is set, the variant should be set according to the
        instance variant.
        """
        placeholder = Placeholder.objects.create(slot="test")

        # Create plugin with a dummy variant
        glimpse_variantized = GlimpseFactory(variant="foo")
        model_instance = add_plugin(
            placeholder,
            GlimpsePlugin,
            "en",
            title=glimpse_variantized.title,
            variant=glimpse_variantized.variant,
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        computed_variant = plugin_instance.compute_variant({}, glimpse_variantized)
        self.assertEqual(computed_variant, "foo")

    def test_cms_plugins_glimpse_compute_variant_with_context_value(self):
        """
        When there is a "variant" value set from template parent, if instance
        variant is empty the variant should adopt the one from template parent
        and if instance variant is set the variant should be set accorded to
        the instance variant.
        """
        placeholder = Placeholder.objects.create(slot="test")

        dummy_context = {
            "glimpse_variant": "ping",
        }

        # Create plugin without a variant
        glimpse_neutral = GlimpseFactory(variant=None)
        model_instance = add_plugin(
            placeholder,
            GlimpsePlugin,
            "en",
            title=glimpse_neutral.title,
            variant=glimpse_neutral.variant,
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        computed_variant = plugin_instance.compute_variant(
            dummy_context, glimpse_neutral
        )
        self.assertEqual(computed_variant, "ping")

        # Create plugin with a dummy variant
        glimpse_variantized = GlimpseFactory(variant="foo")
        model_instance = add_plugin(
            placeholder,
            GlimpsePlugin,
            "en",
            title=glimpse_variantized.title,
            variant=glimpse_variantized.variant,
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        computed_variant = plugin_instance.compute_variant(
            dummy_context, glimpse_variantized
        )
        self.assertEqual(computed_variant, "foo")
