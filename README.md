# CSVsniffer
[![DOI](https://zenodo.org/badge/DOI/10.3233/DS-240062.svg)](https://doi.org/10.3233/DS-240062)

Companion repository for the paper:

[**Detecting CSV File Dialects by Table Uniformity Measurement and Data Type Inference**](https://content.iospress.com/articles/data-science/ds240062) 
[(PDF)](https://content.iospress.com/download/data-science/ds240062?id=data-science%2Fds240062)

by [W. García](https://sciprofiles.com/profile/3400377).

An application of the _Table Uniformity_ method outlined in the paper can be found in the [CSV interface](https://github.com/ws-garcia/VBA-CSV-interface) repository. Also, a Python version using `CleverCSV` source code has been implemented and stored in the `python` folder, demonstrating the reliability of the research presented.

## Introduction

The results from the research can be reproduced by running the `RunTests` method from the macro-enabled Excel workbook `CSVsniffer.xlsm`. To review the results for CleverCSV it is necessary to run the scripts from the `clevercsv_test.py` file. The text files with the results output are stored in the `Current research` and `cleverCSV` folders. Additional results can be read from the `python/tests results/` folder.


## Data

The `CSV` folder contains the files copied from the [Pollock framework](https://github.com/HPI-Information-Systems/Pollock) and other collected test files. Also the dataset used for the [CSV wrangling research](https://github.com/alan-turing-institute/CSV_Wrangling) is available in the `CSV_Wranglin` folder. Note that only link to the files can be provided, in this last case,due to the authors holds the copyright. A dataset from w3c, CSVW project, is available in the `W3C-CSVW` folder. 

The expect configuration for each tested CSV is saved in the `Dialect_annotations.txt`, `Manual_dialect_annotation.txt` and `W3C-CSVW-Dialect_annotations.txt` files.

## Results

In this section, the results after running tests with the Beta Python implementation of the _Table Uniformity_ method are presented.

The table below shows the dialect detection accuracy for both `CSVsniffer` and `CleverCSV`.

|Data set                    |CSVsniffer|CleverCSV|
|:---------------------------|:---------|:--------|
|POLLOCK                     |96.6216%  |94.5946% |
|CSV Wrangling               |88.8158%  |79.5775% |
|CSV Wrangling filtered CODEC|89.4366%  |79.5775% |
|CSV Wrangling MESSY         |78.8732%  |76.9841% |
|W3C-CSVW                    |95.4338%  |59.5238% |

The following table shows the average accuracy for both tools.

|Tool        |Accuracy average|
|:-----------|:---------------|
|`CSVsniffer`|89.84%          |
|`CleverCSV` |78.05%          |

The last table shows the execution times obtained.

|Tool        |Run-time    |
|:-----------|:-----------|
|`CSVsniffer`|95.41 sec.  |
|`CleverCSV` |1067.47 sec.|

The results show that `CSVsniffer`, based on the _Table Uniformity_ method, is a solid candidate to be considered as a utility for reliable dialect detection for CSV files.

## Requirements

Below are the requirements for reproducing the experiments.

- Microsoft Office Excel.
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