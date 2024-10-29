import folium
import unittest
from iris_insee_utils.iris_map import plot_folium_map

class TestFoliumMap(unittest.TestCase):

    def test_plot_folium_map(self):
        # Call the function to generate the map
        map = plot_folium_map(commune_name="Nice", iris_year=2018)

        # Check if the returned object is a Folium Map
        self.assertIsInstance(map, folium.Map)

        # Generate HTML content
        html_content = map.get_root().render()

        print(html_content[:2000])
        # Check if the HTML content contains expected elements
        self.assertIn('<div class="folium-map"', html_content)
        self.assertIn('Nice', html_content)  # Check if the commune name is in the HTML

if __name__ == '__main__':
    unittest.main()