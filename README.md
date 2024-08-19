# CSVsniffer
[![DOI](https://zenodo.org/badge/DOI/10.3233/DS-240062.svg)](https://doi.org/10.3233/DS-240062)

Companion repository for the paper:

[**Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference**](https://content.iospress.com/articles/data-science/ds240062) 
[(PDF)](https://content.iospress.com/download/data-science/ds240062?id=data-science%2Fds240062)

by [W. García](https://sciprofiles.com/profile/3400377).

An application of the _Table Uniformity_ method outlined in the paper can be found in the [CSV interface](https://github.com/ws-garcia/VBA-CSV-interface) repository. Also, a Python version using `CleverCSV` source code has been implemented and stored in the `python` folder, demonstrating the reliability of the research presented.

## Introduction

The results from the research can be reproduced by running the `RunTests` method from the macro-enabled Excel workbook `CSVsniffer.xlsm`. To review the results for CleverCSV it is necessary to run the scripts from the `clevercsv_test.py` file. The text files with the results output are stored in the `Current research` and `cleverCSV` folders. Additional results can be reproduced by running scripts in the `python/src/run_tests.py` file, the results can be read from the `python/tests results/` folder.


## Data

The `CSV` folder contains the files copied from the [Pollock framework](https://github.com/HPI-Information-Systems/Pollock) and other collected test files. Also the dataset used for the [CSV wrangling research](https://github.com/alan-turing-institute/CSV_Wrangling) is available in the `CSV_Wranglin` folder. Note that only link to the files can be provided, in this last case,due to the authors holds the copyright. A dataset from w3c, CSVW project, is available in the `W3C-CSVW` folder. 

The expect configuration for each tested CSV is saved in the `Dialect_annotations.txt`, `Manual_dialect_annotation.txt` and `W3C-CSVW-Dialect_annotations.txt` files.

## Results

In this section, the results after running tests with the Beta Python implementation of the _Table Uniformity_ method are presented. In order to obtain more representative performance metrics, it was decided to run the tests on a system running Linux Mint.

The table below shows the dialect detection success ratio for `CSVsniffer`, `CleverCSV` and the built-in Python `csv.Sniffer` class module. Note that the accuracy has been measured using only those files that do not produce a failure when attempting to infer CSV dialects

|Data set                    |`CSVsniffer` |`CleverCSV`|`csv.Sniffer`|
|:---------------------------|:------------|:----------|:------------|
|POLLOCK                     |96.5517%     |95.1724%   |96.3504%     |
|CSV Wrangling               |90.5660%     |84.3137%   |80.5556%     |
|CSV Wrangling filtered CODEC|89.4737%     |84.2520%   |80.0000%     |
|CSV Wrangling MESSY         |78.1955%     |71.6535%   |66.6667%     |
|W3C-CSVW                    |95.3917%     |61.1111%   |97.6923%     |

The table below shows the failure ratio for each tool.

|Data set                                |`CSVsniffer` |`CleverCSV`|`csv.Sniffer`|
|:---------------------------------------|:------------|:----------|:------------|
|POLLOCK [148 files]                     |2.0270%      |2.0270%    |7.4324%      |
|CSV Wrangling [179 files]               |11.1732%     |14.5251%   |19.5531%     |
|CSV Wrangling filtered CODEC [142 files]|6.3380%      |10.5634%   |15.4930%     |
|CSV Wrangling MESSY [126 files]         |6.3380%      |10.5634%   |15.4930%     |
|W3C-CSVW [221 files]                    |1.8100%      |2.2624%    |41.1765%     |

The following table shows the average success and failure ratio for selected tools. The higher the number of errors obtained, the lower the reliability for detection.

|Tool          |Success ratio (SR)|Failure ratio  (FR)|
|:-------------|:-----------------|:------------------|
|`CSVsniffer`  |90.04%            |5.54%              |
|`CleverCSV`   |79.30%            |7.99%              |
|`csv.Sniffer` |84.25%            |19.83%             |

As a complementary metric, the table below shows the average reliability factor for CSV dialect detection. This value is computed as: 
$$RF=SR\times (1-FR)$$.

|Tool          |Reliability factor (RF)|
|:-------------|:----------------------|
|`CSVsniffer`  |85.05%                 |
|`CleverCSV`   |72.96%                 |
|`csv.Sniffer` |67.54%                 |

The below table shows the execution times obtained. In this one we can see that the Python module, reading 6144 characters from the CSV files, is incredibly efficient, easily outperforming the other tools.

|Tool         |Run-time    |
|:------------|:-----------|
|`csv.Sniffer`|0.98 sec.   |
|`CleverCSV`  |6.54 sec.   |
|`CSVsniffer` |17.00 sec.  |

### Accuracy analysis

For dialect detection, we have defined _True Positive_ (TP) as the number of CSV files where the dialect was correctly detected. By its way, _False Positive_ (FP) is defined as the number of CSV files where the dialect was incorrectly identified as a specific dialect when it was actually a different dialect. _False Negatives_ (FN) is defined as the number of CSV files where the specific dialect was present but not detected.

The next table shows the precision (P), which measures the accuracy of dialect detection when predicting a specific dialect. The metric is calculated as follows

$$P=\frac{TP}{TP+FP}$$

|Data set                     |`CSVsniffer` |`CleverCSV`|`csv.Sniffer`|
|:----------------------------|:------------|:----------|:------------|
|POLLOCK                      |0.9655       |0.9517     |0.9635       |
|CSV Wrangling                |0.9057       |0.8431     |0.8056       |
|CSV Wrangling filtered CODEC |0.8947       |0.8425     |0.8000       |
|CSV Wrangling MESSY          |0.7820       |0.7165     |0.6667       |
|W3C-CSVW                     |0.9539       |0.6111     |0.9769       |

The following table shows the recall (R), which measures the ability of the method to detect the specific dialect when it is actually present. The metric is calculated as follows

$$R=\frac{TP}{TP+FN}$$

|Data set                     |`CSVsniffer` |`CleverCSV`|`csv.Sniffer`|
|:----------------------------|:------------|:----------|:------------|
|POLLOCK                      |0.9790       |0.9787     |0.9231       |
|CSV Wrangling                |0.8780       |0.8323     |0.7682       |
|CSV Wrangling filtered CODEC |0.9297       |0.8770     |0.8136       |
|CSV Wrangling MESSY          |0.9204       |0.8585     |0.7843       |
|W3C-CSVW                     |0.9810       |0.9635     |0.5826       |

The below table shows the F1 score, which is the most polished measure of dialect detection accuracy. The metric is calculated as follows

$$F1=2 \times \frac{P \times R}{P+R}$$

|Data set                     |`CSVsniffer` |`CleverCSV`|`csv.Sniffer`|
|:----------------------------|:------------|:----------|:------------|
|POLLOCK                      |0.9722       |0.9650     |0.9429       |
|CSV Wrangling                |0.8916       |0.8377     |0.7865       |
|CSV Wrangling filtered CODEC |0.9119       |0.8594     |0.8067       |
|CSV Wrangling MESSY          |0.8456       |0.7811     |0.7207       |
|W3C-CSVW                     |0.9673       |0.7479     |0.7299       |

Thus, the True Positive (TP) weighted F1 score for each tool is computed as

$$F1_{Weighted} Score = \frac{\sum_{i=1}^{n} TP_i \times F1_{Score}i}{\sum_{i=1}^{n} TP_i}$$ 

where
- $\text{TP}_i$: The number of True Positive instances of dataset $i$.
- $F1_{Score}i$: The F1 score for dataset $i$.

The computations are given in the below table.

|Tool          |F1 score|
|:-------------|:-------|
|`CSVsniffer`  |0.9260  |
|`CleverCSV`   |0.8425  |
|`csv.Sniffer` |0.8049  |

### Conclusions

By studying the last table it is concluded that the _Table Uniformity_ method is able to predict and determine the dialects of CSV files with an accuracy of 92.60% using a sample of 10 records, while `CleverCSV` can reach 84.25% accuracy by loading 6144 characters.

The proposed methodology shows an improvement of 8.35% over `CleverCSV` using the same source code for data type detection. A substantial improvement could derive from a stricter data detection, reducing the number of false positives detected in cells. On the other hand, `CleverCSV` doesn't shows significant accuracy improvements when reading all the data from the CSV files. This unexpected result helps to reaffirm that dialect detection does not always require reading all the information from the CSV files. 

So we can conclude that the _Table Uniformity_ method is the ideal candidate to be implemented as the default dialect detection method of the Python `csv` module, despite the fact that the increased accuracy leads to an increase in execution time, as shown in a previous table. An alternative would be to use `Pandas` to avoid the overhead of using the file iterator to pre-filter the lines to be used in the creation of the tables to be evaluated. 

## Requirements

Below are the requirements for reproducing the experiments.

- Microsoft Office Excel.
- Python v3
- [CleverCSV](https://github.com/alan-turing-institute/CleverCSV) and all its dependencies.

## Credits

Many of the CSV files used in this research were recovered from different repositories. Below you can review the list.
- [x] franciscom/testlink-code-playground/
- [x] boryn/yii_demo/
- [x] dengkeaway/kunagi/
- [x] austinrfnd/arethedodgersplayingtonight.com/
- [x] okfn/messytables/
- [x] kmugglet/Reporting/
- [x] jankvak/Schedule-of-pain/
- [x] kamilklw/onlineDR/
- [x] mavcunha/dojosp/
- [x] evenwestvang/skoolgate/
- [x] shalomb/dotfiles/
- [x] ockam/php-csv/
- [x] code34/war-in-takistan/
- [x] thejesusbr/GPU-Color2Gray/
- [x] zardosht/clustering/
- [x] bryanburgers/personal-site/
- [x] godlessendeavor/MultiDB/
- [x] vofp/Relation-Browser-Ruby/
- [x] javierfdr/Endrov-collaboration/
- [x] nmklong/limesurvey-cdio3/
- [x] jkamenik/Rails-Profiler/
- [x] philogb/philogb.github.com/
- [x] jaredcohe/sec_scrape/
- [x] andrewxhill/MOL/
- [x] abelhegedus/Magic-Collection-Builder/
- [x] Momus/Multipass/
- [x] christhorpe/gacscraper/
- [x] ikharlampenkov/gkh/
- [x] jekozyra/ngo-project/
- [x] dynamicpacket-public/opensips/
- [x] ryzhov/ATS0/
- [x] pejo751/sube751/
- [x] markkimsal/agent-ohm/
- [x] ericpaulbishop/gargoyle/
- [x] Dopi/JetPlatform/
- [x] jburks/OpenDidj/
- [x] matsubo/emoji-sprite/
- [x] 19maps/getWeather/
- [x] athomason/perl-Memcached-libmemcached/
- [x] nadavoid/ReadySiteBase/
- [x] lagenar/rivadavia/
- [x] DAISUKEICHIKAWA/pred/
- [x] mhausenblas/schema-org-rdf/
- [x] mhausenblas/omnidator/
- [x] shinichinomura/zipcode_jp-python/
- [x] bashofmann/opensocial_demo_game/
- [x] rajkosto/mxoemu/
- [x] pino1068/riskman/
- [x] rocksolidwebdesign/AweCMS/
- [x] duckduckgo/zeroclickinfo-goodies/
- [x] jeffreyhorner/coloring/
- [x] ivanistheone/Latent-Dirichlet-Allocation/
- [x] mvilrokx/BPAD/
- [x] navid/Nav/
- [x] lboaretto/Stratos/
- [x] robertogds/ReallyLateBooking/
- [x] regdog/goodlife/
- [x] danux/django-holding-page/
- [x] popdevelop/snapplr/
- [x] MichaelMarner/Half-Real-Scenes/
- [x] bjpop/website/
- [x] dvydra/coupon-rails/
- [x] aaronzhang/kunagi/
- [x] tbielawa/py-prtstat/
- [x] tricycle/electrodrive-market-analysis/
- [x] darpified/kunagi/
- [x] jgarciagarrido/SegoviaOpenTeam/
- [x] datenspiel/is_csv_importable/
- [x] cgueret/eRDF/
- [x] zikula-modules/Eternizer/
- [x] azizmb/TWSS/
- [x] kms/ds1052e-measurements/
- [x] pphetra/fresh-odhd/
- [x] levivya/investmarketkz/
- [x] TeamImba/MDAS/
- [x] saghul/sipp-scenarios/
- [x] wliao008/mysteryleague/
- [x] mgius/cpe458/
- [x] ecell/ecell3-spatiocyte/
- [x] gnorsilva/frontlinesms-core/
- [x] tonytian33/shoppinglist/
- [x] Airead/excise/
- [x] UncleCJ/alexastuff/
- [x] colinmollenhour/magento-lite/
- [x] barbie/test-xhtml/
- [x] kyr0/ExtZF/
- [x] petewarden/dstkdata/
- [x] lacimol/kunagi/
- [x] apslab/ap-manager/
- [x] noosamad/mxp-consolidate/
- [x] practicalparticipation/IKMLinkedResearch/
- [x] cwegrzyn/RHIPE/
- [x] nadineproject/nadine/
- [x] samsonjs/samhuri.net/
- [x] kcampos/Kuali-Sakai-Functional-Test-Automation-Framework/
- [x] max7255/FPGA-Analyzer/
- [x] LATC/sandbox/
- [x] jeffkit/autoforms/
- [x] d8agroup/metaLayer-Gateway/
- [x] hmgaspar/eesddp/
- [x] fadzril/freelovr/
- [x] fguillen/simplecov-csv/
- [x] aminin/google-api-adwords-php/
- [x] michaeltyson/potionstore/9
- [x] srveit/distance/
- [x] zarma/baghdad01/
- [x] hippiefahrzeug/jeannie/
- [x] digitalfox/py10n/
- [x] JanHoralik/jh-prototypes/
- [x] alexmajy/flashcards/
- [x] onlytiancai/codesnip/
- [x] vofp/relation-browser/
- [x] Error-331/Axis-modules/
- [x] CarnegieLearning/MathFluency/
- [x] i-dcc/allele_image/
- [x] hogi/kunagi/
- [x] BarbaraEMac/TrivBot/
- [x] Wisser/Jailer/
- [x] jasonlong/benfords-law/
- [x] soccermetrics/marcotti-sql/
- [x] kennym/itools/
- [x] rkoeppl/skeinforge_settings/
- [x] aalzola/prueba/
- [x] cmheisel/kardboard/
- [x] gfalav/newcar/
- [x] PabloCastellano/pablog-scripts/
- [x] elle/music-library/
- [x] oppian/xerobis/
- [x] twidi/satchmo/
- [x] 34/T/
- [x] apache/bigtop/
- [x] ciriarte/laundry/
- [x] romanchyla/montysolr/
- [x] alibezz/SNRails_Research/
- [x] SQLServerIO/IometerParser/
- [x] renduples/alibtob/
- [x] evanleonard/kunagi/
- [x] yuvadm/ayalon-dat/
- [x] marplatense/erlang/
- [x] spazm/Iron-Munger/
- [x] crschmidt/haitibrowser/
- [x] eLBirador/AllAboutCity/
- [x] Coalas/apsilesia/
- [x] emelleme/All-Drag-Racing/
- [x] despesapublica/site/
- [x] apkennedy/Emmaus-Silverstripe/
- [x] Coalas/kolakowski/
- [x] notioncollective/
- [x] emelleme/G8-life/
- [x] mgc544/sscustom-tra/
- [x] andyinabox/Beyond-the-Debt-Ceiling/
- [x] emelleme/PhillyOpen/
- [x] sponsoredlinx/Total-Care-Asphalting/
- [x] davidmontgomery/Wireframe/
- [x] frappe/frappe/
- [x] davedash/SUMO-issues/
- [x] Habrok/HelloWorld/
- [x] gaubert/java-balivernes/
- [x] befair/gasistafelice/
- [x] komagata/cloister/
- [x] ryannscy/Unemployment-Chart/
- [x] guylhem/PerlMSI/
- [x] lightspeedretail/webstore/
- [x] naderman/symfony/
- [x] orchestra-io/sample-symfony2/
- [x] biow0lf/prometheus2.0/
- [x] sctape/GrinnellPlans/
- [x] joshuabenuck/eshell/
- [x] cmcginn/Common/
- [x] ruby-rdf/sparql-client/
- [x] doubi/Text-CSV_XS/
- [x] cpf-se/citrus/
- [x] abhishekkr/
- [x] NeoGeographyToolkit/kraken/
- [x] denisoid/homebank_import_scripts/
- [x] Jazzinghen/spamOSEK/
- [x] DiUS/java-api-bindings/
- [x] ikko/hazaitop/
- [x] blancavg/ggplot2-basics/
- [x] learnstream/ls_atomic/
- [x] pdawczak/onko/
- [x] peterkrenn/spit-generator/
- [x] TasteeWheat/mxoemu1/
- [x] digitarald/redracer/
- [x] Ezku/xi-framework/
- [x] item/sugarcrm_dev/
- [x] candidasa/silverstripe-phpunit-3.4/
- [x] EHER/phpunit-all-in-one/
- [x] gsdevme-archive/CURL/
- [x] vivid-planet/library/
- [x] psawaya/CS34-Bus-Routing/
- [x] headius/jruby-cdc/
- [x] sbourdeauducq/milkymist-ruby/
- [x] hamhei/hamcolor/
- [x] johnl/deb-ruby1.9.1/
- [x] darealcaffeine/first_app/
- [x] srirammca53/update_status/
- [x] nikuuchi/oreore_ruby/
- [x] Pettrov/Asynchronous-Operations-Module--PHP-/
- [x] TeamRocketScience/Claroline-TRS-Edition/
- [x] khjgbkbk/CRMS/
- [x] milandobrota/WPSocialNetwork/
- [x] cciechad/brlcad/
- [x] mattmccray/gumdrop/
- [x] irace/irace.github.com/
- [x] ronny/kodepos/
- [x] Juuro/Dreamapp-Website/
- [x] Belarus/Windows.OmegaT/
- [x] tuxnani/pyrhmn/
- [x] cesine/ToolsForFieldLinguistics/
- [x] mathics/Mathics/
- [x] jwiegley/CSV2Ledger/
- [x] jmlegr/GestComp/
- [x] mchelen/data_gov_catalog_data/
- [x] jasherai/maatkit/
- [x] cwarden/kettle/
- [x] purpleKarrot/wowmapview/
- [x] egonz/old_sql/
- [x] johnantoni/old.tutorials/
- [x] code-mangler/my-emacs-package/
- [x] calle/fn/
- [x] matthewfarrell/gargoyle/
- [x] e2thex/hackunteers.org/
- [x] andrewjpage/freezer_tracking/
- [x] fbacall/simple-spreadsheet-extractor/
- [x] simonvh/gimmemotifs/
- [x] disnet/contracts.js/
- [x] eckes/wandern/
- [x] zxvf/--2/
- [x] tyage/town-cake/
- [x] whiteshark/kunagi/
- [x] Surgeon/Watir/
- [x] cawka/DSMS_NBC/
- [x] dptww1/WW1AirMap2/
- [x] jonibo/ledgersmb/
- [x] dlc/ttcsbrandon/
- [x] akariv/obudget2/
- [x] meloun/py_ewitis/
- [x] semantic-im/sim-rf/
- [x] sankroh/django-form-manager/
- [x] JudoWill/pyMutF/
- [x] jou4/parsure/
- [x] shanx/djangocon.eu/
- [x] paulgessinger/fermi/
- [x] ajpalkovic/b2010/
- [x] OhTu-IDDQD/scheduler3000/
- [x] OlliD/DtwSequenceCompare/
- [x] lukeorland/phonography/
- [x] r0ck3y3/AAI/
- [x] glenbot/beerapp/
- [x] StephanHoyer/magento-lucene/
