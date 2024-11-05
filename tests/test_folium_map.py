import os
import unittest

import folium
import pandas as pd

from iris_insee_utils.iris_map import plot_folium_map


class TestFoliumMap(unittest.TestCase):

    def test_plot_folium_map(self) -> None:
        # Call the function to generate the map
        m = plot_folium_map(commune_name="Nice", iris_year=2018)

        # Check if the returned object is a Folium Map
        assert isinstance(m, folium.Map)

        # Generate HTML content
        html_content = m.get_root().render()

        # Check if the HTML content contains expected elements
        assert '<div class="folium-map"' in html_content
        assert "Nice" in html_content  # Check if the commune name is in the HTML

    def test_plot_folium_map_with_df_oi(self) -> None:
        df_oi = pd.DataFrame(
            {
                "Lieu": ["Mairie de Marseille", "Site-Mémorial du Camp des Milles"],
                "lon": [5.369905252590892, 5.382786610618382],
                "lat": [43.296630332564405, 43.5034655315141],
            },
        )

        m = plot_folium_map(iris_year=2018, commune_name="Marseille", df_oi=df_oi)
        assert isinstance(m, folium.Map)

    def test_plot_folium_map_df_enrich(self) -> None:
        df_oi = pd.DataFrame(
            {
                "Lieu": ["Mairie de Marseille", "Site-Mémorial du Camp des Milles"],
                "lon": [5.369905252590892, 5.382786610618382],
                "lat": [43.296630332564405, 43.5034655315141],
            },
        )

        df_enrich = pd.DataFrame(
            {"CODE_IRIS": ["132020301", "130010905"], "Some_IRIS_Data": [100, 200]},
        )


        m = plot_folium_map(
            iris_year=2018,
            commune_name="Marseille",
            df_oi=df_oi,
            df_enrich=df_enrich,
            df_enrich_iriscol_colname="CODE_IRIS",
            df_enrich_select_cols=["Some_IRIS_Data"],
        )

        assert isinstance(m, folium.Map)


def test_plot_folium_map() -> None:
    save_map_path = "test_map.html"
    m = plot_folium_map(
        commune_name="Nice", iris_year=2018, save_map_path=save_map_path,
    )

    assert isinstance(m, folium.Map)
    assert os.path.exists(save_map_path)

    # Clean up
    os.remove(save_map_path)


if __name__ == "__main__":
    unittest.main()
