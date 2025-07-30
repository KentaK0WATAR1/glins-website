# publications/views.py
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.views.generic import ListView
from .models import Publication




# ---- 論文リスト ----
# PUBS = [
#     {
#         "slug": "ghg-pricing-international-shipping",
#         "title": "Modelling global and regional economic impacts of greenhouse gas pricing on international shipping and policy implications",
#         "authors": "Tran T.T.; Morimoto S.; Shibasaki R.",
#         "year": 2025,
#         "type": "Journal article",
#         "doi": "10.1016/j.ocecoaman.2025.107804",
#         "pdf": "",
#     },
#     {
#         "slug": "routing-dry-bulk-nsr-scr",
#         "title": "Optimum routing for dry bulk voyages with the effect of an emission trading system: NSR vs SCR",
#         "authors": "Kavirathna C.A.; Shibasaki R.; Ding W.",
#         "year": 2025,
#         "type": "Journal article",
#         "doi": "10.1016/j.clscn.2025.100224",
#         "pdf": "",
#     },
#     {
#         "slug": "ais-geospatial-spot-drybulk",
#         "title": "AIS-based geospatial analysis on spot contract of dry bulk carriers",
#         "authors": "Tran T.T.T.; Murong L.; Liu L.; Shibasaki R.",
#         "year": 2025,
#         "type": "Journal article",
#         "doi": "10.1016/j.rtbm.2025.101315",
#         "pdf": "",
#     },
#     {
#         "slug": "mode-competitiveness-speed-optimization",
#         "title": "How should mode competitiveness and profit be balanced in maritime transport? – Vessel speed optimization approach including Northern Sea Route",
#         "authors": "Ding W.; Shibasaki R.; Kavirathna C.A.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.1080/03088839.2024.2417823",
#         "pdf": "",
#     },
#     {
#         "slug": "co2-reduction-hinterland-japan",
#         "title": "Scenario analysis on CO2 emission reductions in hinterland transport of Japan through intermodal logistics network simulation",
#         "authors": "Matsuyama R.; Sugimura Y.; Shibasaki R.; Tran T.T.T.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.1016/j.jclepro.2024.142503",
#         "pdf": "",
#     },
#     {
#         "slug": "vessel-trains-feasibility",
#         "title": "Assessment of the feasibility of vessel trains in the ocean shipping sector",
#         "authors": "Liu L.; Liu K.; Shibasaki R.; Zhang Y.; Zhang M.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.1016/j.trd.2024.104188",
#         "pdf": "",
#     },
#     {
#         "slug": "terminal-congestion-satellite-ais",
#         "title": "Terminal congestion analysis of container ports using satellite images and AIS",
#         "authors": "Yasuda K.; Shibasaki R.; Yasuda R.; Murata H.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.3390/rs16061082",
#         "pdf": "",
#     },
#     {
#         "slug": "corridor-development-south-asia",
#         "title": "How do corridor development and border facilitation policies impact future container transport in inland South Asia? – A network simulation approach",
#         "authors": "Kawachi K.; Shibasaki R.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.1016/j.ajsl.2024.01.003",
#         "pdf": "",
#     },
#     {
#         "slug": "ais-forecast-drybulk-throughput",
#         "title": "Can AIS data improve the short-term forecast of weekly dry bulk cargo port throughput? – A machine-learning approach",
#         "authors": "Nakashima M.; Shibasaki R.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.1080/03088839.2023.2212264",
#         "pdf": "",
#     },
#     {
#         "slug": "cambodian-logistics-policy-impact",
#         "title": "Impact of Cambodian international logistics policies on container cargo flow in comprehensive intermodal transport network",
#         "authors": "Kosuge N.; Shibasaki R.; Sanui K.; Okubo K.",
#         "year": 2024,
#         "type": "Journal article",
#         "doi": "10.1080/13675567.2021.1967898",
#         "pdf": "",
#     },
#     {
#         "slug": "bunkering-services-ais",
#         "title": "Extraction of bunkering services from Automatic Identification System data and their international comparisons",
#         "authors": "Watanabe E.; Shibasaki R.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.3390/su152416711",
#         "pdf": "",
#     },
#     {
#         "slug": "nsr-feasibility-ecm",
#         "title": "Feasibility of the Northern Sea Route with the effect of Emission Control Measures",
#         "authors": "Kavirathna C.A.; Shibasaki R.; Ding W.; Otsuka N.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.1016/j.trd.2023.103896",
#         "pdf": "",
#     },
#     {
#         "slug": "nighttime-light-terminal-status",
#         "title": "Identifying the operational status of container terminals from high-resolution nighttime-light satellite image for global supply chain network optimization",
#         "authors": "Murata H.; Shibasaki R.; Imura N.; Nishinari K.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.3389/frsen.2023.1229745",
#         "pdf": "",
#     },
#     {
#         "slug": "west-africa-logistics-simulation",
#         "title": "Stagnant logistics growth simulation on West African intermodal corridors",
#         "authors": "Shibuya K.; Shibasaki R.; Kawasaki T.; Tokuori T.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.1016/j.trip.2023.100867",
#         "pdf": "",
#     },
#     {
#         "slug": "intermodal-network-myanmar",
#         "title": "Global logistics intermodal network simulation modeling by incremental assignment and corridor development simulations in Myanmar",
#         "authors": "Yamaguchi T.; Kawachi K.; Shibuya K.; Hagiwara M.; Shibasaki R.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.1016/j.eastsj.2023.100114",
#         "pdf": "",
#     },
#     {
#         "slug": "intra-asian-network-structure",
#         "title": "Modeling structural changes in intra-Asian maritime container shipping networks considering their characteristics",
#         "authors": "Shibuya K.; Shibasaki R.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.3390/su151310055",
#         "pdf": "",
#     },
#     {
#         "slug": "nsr-china-grain-imports",
#         "title": "Impact of Northern Sea Route on China’s grain imports with EU countries",
#         "authors": "Ding W.; Shibasaki R.; Kavirathna C.A.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.1016/j.eastsj.2023.100108",
#         "pdf": "",
#     },
#     {
#         "slug": "data-driven-shipping-networks",
#         "title": "Data-driven framework for extracting global maritime shipping networks by machine learning",
#         "authors": "Liu L.; Shibasaki R.; Zhang Y.; Kosuge N.; Zhang M.; Hu Y.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.1016/j.oceaneng.2022.113494",
#         "pdf": "",
#     },
#     {
#         "slug": "container-networks-1969-1981",
#         "title": "Global maritime container shipping networks 1969–1981: Emergence of container shipping and reopening of the Suez Canal",
#         "authors": "Saito T.; Shibasaki R.; Murakami S.; Tsubota K.; Matsuda T.",
#         "year": 2022,
#         "type": "Journal article",
#         "doi": "10.3390/jmse10050602",
#         "pdf": "",
#     },
#     {
#         "slug": "hakata-port-strategy-simulation",
#         "title": "Logistics strategy simulation of second-ranked ports on the basis of Japan’s port reforms: A case study of Hakata Port",
#         "authors": "Sugimura Y.; Wakashima H.; Liang Z.; Shibasaki R.",
#         "year": 2023,
#         "type": "Journal article",
#         "doi": "10.1080/03088839.2022.2057610",
#         "pdf": "",
#     },
#     {
#         "slug": "african-trade-scenario-planning",
#         "title": "Predicting African trade considering uncertainty by scenario planning",
#         "authors": "Shibasaki R.; Abe M.; Sato W.; Otani N.; Nakagawa A.; Onodera H.",
#         "year": 2022,
#         "type": "Journal article",
#         "doi": "10.1108/MABR-07-2021-0056",
#         "pdf": "",
#     },
#     {
#         "slug": "ecommerce-covid-japan",
#         "title": "How the use and acceptance of e-commerce was affected by the COVID-19 outbreak – A Japanese case",
#         "authors": "Wakashima H.; Kawasaki T.; Shibasaki R.",
#         "year": 2022,
#         "type": "Journal article",
#         "doi": "10.11175/easts.14.845",
#         "pdf": "",
#     },
#     {
#         "slug": "ecommerce-panel-japan",
#         "title": "The use of e-commerce and the COVID-19 outbreak: A panel data analysis in Japan",
#         "authors": "Kawasaki T.; Wakashima H.; Shibasaki R.",
#         "year": 2022,
#         "type": "Journal article",
#         "doi": "10.1016/j.tranpol.2021.10.023",
#         "pdf": "",
#     },
#     {
#         "slug": "foldable-containers-repositioning",
#         "title": "Do foldable containers enhance efficient empty container repositioning under demand fluctuation? ―Case of the Pacific region",
#         "authors": "Liang Z.; Shibasaki R.; Hoshino Y.",
#         "year": 2021,
#         "type": "Journal article",
#         "doi": "10.3390/su13094730",
#         "pdf": "",
#     },
#     {
#         "slug": "arctic-shipping-systematic-review",
#         "title": "Economic feasibility of Arctic shipping from multiple perspectives: a systematic review",
#         "authors": "Kavirathna C.A.; Shibasaki R.",
#         "year": 2021,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "gms-corridor-logistics",
#         "title": "Impact on Myanmar’s logistics efficiency of the East–West and Southern Corridor development of the Greater Mekong Subregion – A global logistics intermodal network simulation",
#         "authors": "Yamaguchi T.; Shibasaki R.; Samizo H.; Ushirooka H.",
#         "year": 2021,
#         "type": "Journal article",
#         "doi": "10.3390/su13020668",
#         "pdf": "",
#     },
#     {
#         "slug": "south-asia-intermodal-network",
#         "title": "International intermodal container shipping network in South Asia: Modelling and policy simulations",
#         "authors": "Shibasaki R.; Kawasaki T.",
#         "year": 2021,
#         "type": "Journal article",
#         "doi": "10.1504/IJSTL.2021.112916",
#         "pdf": "",
#     },
#     {
#         "slug": "maritime-bigdata-analysis",
#         "title": "Can maritime big data be applied to shipping industry analysis? – Focusing on commodities and vessel sizes of dry bulk carriers",
#         "authors": "Kanamoto K.; Murong L.; Nakashima M.; Shibasaki R.",
#         "year": 2021,
#         "type": "Journal article",
#         "doi": "10.1057/s41278-020-00171-6",
#         "pdf": "",
#     },
#     {
#         "slug": "lng-supplychain-port-based",
#         "title": "Estimating global pattern of LNG supply chain: A port-based approach by vessel movement database",
#         "authors": "Shibasaki R.; Kanamoto K.; Suzuki T.",
#         "year": 2020,
#         "type": "Journal article",
#         "doi": "10.1080/03088839.2019.1657974",
#         "pdf": "",
#     },
#     {
#         "slug": "gwadar-port-bri",
#         "title": "Could Gwadar port in Pakistan be a new gateway? – A network simulation approach in the context of the Belt and Road Initiative",
#         "authors": "Tanabe S.; Shibasaki R.; Kato H.; Lee P.T.-W.",
#         "year": 2019,
#         "type": "Journal article",
#         "doi": "10.3390/su11205757",
#         "pdf": "",
#     },
#     {
#         "slug": "south-asia-transhipment-hub",
#         "title": "A transhipment hub in South Asia and its competition: Application of network equilibrium assignment model for global maritime container shipping",
#         "authors": "Shibasaki R.; Kawasaki T.",
#         "year": 2019,
#         "type": "Journal article",
#         "doi": "10.11175/eastsats.5.546",
#         "pdf": "",
#     },
#     {
#         "slug": "nsr-panama-lng-market",
#         "title": "How do the new shipping routes affect Asian LNG markets and economy? – Case of the Northern Sea Route and Panama Canal Expansion",
#         "authors": "Shibasaki R.; Usami T.; Furuichi M.; Teranishi H.; Kato H.",
#         "year": 2018,
#         "type": "Journal article",
#         "doi": "10.1080/03088839.2018.1445309",
#         "pdf": "",
#     },
#     {
#         "slug": "drybulk-route-choice-suez",
#         "title": "Global route choice and its modelling of dry bulk carriers based on vessel movement database: focusing on the Suez Canal",
#         "authors": "Shibasaki R.; Azuma T.; Yoshida T.; Teranishi H.; Abe M.",
#         "year": 2017,
#         "type": "Journal article",
#         "doi": "10.1016/j.rtbm.2017.08.003",
#         "pdf": "",
#     },
#     {
#         "slug": "container-transit-mekong",
#         "title": "Implications for Better Container Transit in the Lower Mekong River through the Field Survey and Policy Simulation",
#         "authors": "Shimada T.; Shibasaki R.; Kume H.; Suzuki M.",
#         "year": 2017,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "network-assignment-central-america",
#         "title": "Network assignment model of integrating maritime and hinterland container shipping: application to Central America",
#         "authors": "Shibasaki R.; Iijima T.; Kawakami T.; Kadono T.; Shishido T.",
#         "year": 2017,
#         "type": "Journal article",
#         "doi": "10.1057/s41278-016-0055-3",
#         "pdf": "",
#     },
#     {
#         "slug": "containership-route-choice",
#         "title": "Route Choice of Containership on a Global Scale and Model Development: Focusing on the Suez Canal",
#         "authors": "Shibasaki R.; Azuma T.; Yoshida T.",
#         "year": 2016,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "infrastructure-impact-central-asia",
#         "title": "Impact assessment model of international transportation infrastructure development: Focusing on trade and freight traffic in Central Asia",
#         "authors": "Tanabe S.; Shibasaki R.; Kato H.",
#         "year": 2016,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "risk-perception-fukushima-maritime",
#         "title": "Risk Perception and Communication at Maritime Transportation to and from Japan after the Fukushima Daiichi Nuclear Power Plant Disaster",
#         "authors": "Wang X.; Kato H.; Shibasaki R.",
#         "year": 2013,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "straits-malacca-risk-impact",
#         "title": "Potential Impacts of Maritime Transportation Risk at the Straits of Malacca and Singapore on Maritime Traffic Flows and Regional Economies",
#         "authors": "Kato H.; Shibasaki R.; Nakamura K.; Ogawa Y.",
#         "year": 2013,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "apec-trade-forecast",
#         "title": "Future Forecast of Trade Amount and International Cargo Flow in the APEC Region: An Application of Trade-Logistics Forecasting Model",
#         "authors": "Shibasaki R.; Watanabe T.",
#         "year": 2012,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "infrastructure-gms-freight-traffic",
#         "title": "Influence of Transportation Infrastructure Development on Freight Traffic Flow Patterns in GMS",
#         "authors": "Iwata T.; Kato H.; Shibasaki R.",
#         "year": 2012,
#         "type": "Book chapter",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "roro-simulation-eastern-asia",
#         "title": "International Ferry and RORO Ship Simulation in Eastern Asia using Intermodal Freight Flow Model",
#         "authors": "Shibasaki R.; Fujiwara T.",
#         "year": 2012,
#         "type": "Conference paper",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "model-accuracy-freight-simulation",
#         "title": "How is Model Accuracy Improved by Usage of Statistics? – An Example of International Freight Simulation Model in East Asia",
#         "authors": "Shibasaki R.; Watanabe T.; Araki D.",
#         "year": 2010,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "china-trade-forecast",
#         "title": "Future Forecast of Chinese Trade Amount and International Cargo Flow",
#         "authors": "Shibasaki R.; Watanabe T.",
#         "year": 2010,
#         "type": "Conference paper",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "semi-trailer-transport-japan-korea",
#         "title": "A Comparison of Semi-Trailer Transport of International Maritime Container Cargo in Japan and South Korea, and its implications",
#         "authors": "Shibasaki R.; Kawasaki T.; Sugiyama S.; Akakura Y.",
#         "year": 2010,
#         "type": "Conference paper",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "pearl-river-simulation",
#         "title": "Container cargo simulation modeling for measuring impacts of infrastructure investment projects in Pearl River Delta",
#         "authors": "Li J.; Shibasaki R.; Li B.",
#         "year": 2010,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "bottlenecks-container-japan",
#         "title": "An Analysis on Bottlenecks for Domestic Vehicular Transportation of International Maritime Container Cargos in Japanese Hinterland",
#         "authors": "Watanabe T.; Shibasaki R.; Nakajima H.; Sugiyama S.; Ochi D.; Akakura Y.",
#         "year": 2008,
#         "type": "Conference paper",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "chinese-port-policy-impact",
#         "title": "Impact of Chinese Port Policy Using the Model for International Container Cargo Simulation",
#         "authors": "Shibasaki R.; Kannami Y.; Onodera H.; Li J.",
#         "year": 2007,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "container-simulation-china-ports",
#         "title": "Simulation of the International Container Cargo Movement in Chinese Ports by Incorporating Chinese Land Transport Network",
#         "authors": "Ma L.; Shibasaki R.; Ieda H.",
#         "year": 2006,
#         "type": "Conference paper",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "gtap-container-volumes-asia",
#         "title": "Estimation of the International Container Shipping Transport Volumes among Asian Countries by Global Trade Analysis Project Model and Its Applications on FTA and Transport Improvement Scenarios",
#         "authors": "Ma L.; Shibasaki R.",
#         "year": 2005,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "container-shipping-model-east-asia",
#         "title": "Model Development for East Asian Container Shipping Considering Multifarious Use of Vessels and Ports",
#         "authors": "Ieda H.; Shibasaki R.; Naito S.; Mishima D.",
#         "year": 2000,
#         "type": "Conference paper",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "cognitive-effects-disaster-investments",
#         "title": "Measurement of Cognitive Effects Against Disaster / Accident Risk from Actual Social Investments",
#         "authors": "Shibasaki R.; Kamei K.; Tanaka H.; Ieda H.",
#         "year": 2001,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
#     {
#         "slug": "risk-evaluation-intersections",
#         "title": "Risk Evaluation Model for Traffic Accident at Four-Legged Signalized Intersections",
#         "authors": "Karim D.M.; Ieda H.; Terabe S.; Shibasaki R.",
#         "year": 2001,
#         "type": "Journal article",
#         "doi": "",
#         "pdf": "",
#     },
# ]

# # ---- 一覧表示 ----
# class PublicationListView(ListView):
#     model               = Publication
#     template_name       = "publications/publication_list.html"
#     context_object_name = "pubs"
#     paginate_by         = 12
# class PublicationListView(TemplateView):
#     template_name = "publications/publication_list.html"
#     paginate_by   = 12

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)

#         # 手動でページネート
#         paginator  = Paginator(PUBS, self.paginate_by)
#         page_num   = self.request.GET.get("page")
#         try:
#             page_obj = paginator.page(page_num)
#         except PageNotAnInteger:
#             page_obj = paginator.page(1)
#         except EmptyPage:
#             page_obj = paginator.page(paginator.num_pages)

#         ctx["pubs"]         = page_obj.object_list
#         ctx["page_obj"]     = page_obj
#         ctx["is_paginated"] = page_obj.has_other_pages()
#         return ctx
    
class PublicationListView(ListView):
    model               = Publication
    template_name       = "publications/publication_list.html"
    context_object_name = "pubs"
    paginate_by         = 12        # そのまま

    def get_queryset(self):
        return super().get_queryset().only(
            "title", "authors", "year", "doi"
        )


class PublicationDetailView(TemplateView):
    # あなたのファイル名に合わせる
    template_name = "publications/publication_detail.html"

    def get_context_data(self, **kwargs):
        ctx  = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]

        # スラッグが一致する辞書を取り出す
        try:
            ctx["pub"] = next(p for p in PUBS if p["slug"] == slug)
        except StopIteration:
            raise Http404("Publication not found")

        return ctx