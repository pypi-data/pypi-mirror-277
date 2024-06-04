ROOSTER training framework (MSAP4-03)
=====================================

This notebook provide an example of the analysis of a set of stars with
catalog-existing reference :math:`P_\mathrm{rot}`, and use the set to
train an instance of ROOSTER.

First we need to import the demonstrator module and the auxiliary module
containing the dataset we are going to work with.

**Note:** This notebook has been designed for the purpose of scientific
justification of PLATO MSAP4-03. The notebook illustrated the precise
flowchart envisaged for PLATO MSAP4-03 is cs_rooster_sph_analysis.ipynb

.. code:: ipython3

    import star_privateer as sp
    import plato_msap4_demonstrator_datasets.kepler_dataset as kepler_dataset

.. code:: ipython3

    sp.__version__




.. parsed-literal::

    '1.1.2'



We also need to import some other modules to run the notebook and to
check that the outputs directory that we need exist. In addition to
``star_privateer`` requirements, you should make sure that the
```pathos``
module <https://pathos.readthedocs.io/en/latest/index.html>`__ is
installed in order to run the analysis in parallel.

.. code:: ipython3

    import os, pathos
    import numpy as np
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    
    if not os.path.exists ('rooster_training_features') :
        os.mkdir ('rooster_training_features')
    if not os.path.exists ('rooster_instances') :
        os.mkdir ('rooster_instances')

Running the analysis pipeline
-----------------------------

We are going to work with a sample of 1991 *Kepler* stars analysed by
Santos et al. (2019, 2021). The light curves have been calibrated with
the KEPSEISMIC method (see García et al. 2011, 2014), and all of them
have been filtered with a 55-day high-pass filter. We can get the
identifiers of the stars in the dataset with the following instruction:

.. code:: ipython3

    list_kic = sp.get_list_targets (kepler_dataset)

The next step is to run the analysis pipeline on every light curve in
the dataset. The analysis pipeline in its default behaviour will compute
the Lomb-Scargle periodogram (LSP) of the light curve as well as its
auto-correlation function (ACF). ACF and LSP will then be used to
compute a composite spectrum (CS), obtained by multiplying one by
another. The feature computed for each stars are stored in a dedicated
csv file identified by the star identifier (in this case, the KIC of the
star). We are going to parallelise the analysis process with ``pathos``
in order to gain some computation time and control memory leakages that
could arise from calling ``analysis_pipeline`` in a loop.

.. code:: ipython3

    def analysis_wrapper (kic) :
        """
        Analysis wrapper to speed computation
        by parallelising process and control
        memory usage.
        """
        str_kic = str (kic).zfill (9)
        filename = sp.get_target_filename (kepler_dataset, str_kic)
        fileout = 'rooster_training_features/{}.csv'.format(str_kic)
        fileplot = 'rooster_training_features/{}.png'.format(str_kic)
        if not os.path.exists (fileout) :
            t, s, dt = sp.load_resource (filename)
            (p_ps, p_acf, 
             ps, acf, 
             cs, features, 
             feature_names, 
             fig) = sp.analysis_pipeline (t, s, pmin=0.1, pmax=60,
                                          wavelet_analysis=False, plot=True,
                                          filename=fileplot, figsize=(10,16), 
                                          lw=1, dpi=300, pfa_threshold=1e-6)
            df = sp.save_features (fileout, kic, features, feature_names)
            plt.close ("all")

Now that are wrapper function is defined, we just create a
``ProcessPool`` that we run with ``imap``:

   Note: by default ``imap``, on the contrary to ``map``, is a
   non-blocking process. Nevertheless, in order to display a progress
   bar with ``tqdm`` we need to use it, and the ``list`` encapsulation
   is there to ensure the process is blocking.

.. code:: ipython3

    process_pool = pathos.pools._ProcessPool (processes=4, 
                                              maxtasksperchild=10)
    with process_pool as p :
        list (tqdm (p.imap (analysis_wrapper,
                            list_kic,
                            ),
                    total=len (list_kic))
              )
        p.close ()


.. parsed-literal::

    100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1991/1991 [00:02<00:00, 682.41it/s]


After running the analysis pipeline, it is possible to concatenate the
feature obtained for each star into one big DataFrame.

.. code:: ipython3

    df = sp.build_catalog_features ('rooster_training_features')

This is typically what the DataFrame is going to look like:

.. code:: ipython3

    df




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>prot_ps</th>
          <th>prot_acf</th>
          <th>prot_cs</th>
          <th>e_prot_ps</th>
          <th>E_prot_ps</th>
          <th>e_prot_acf</th>
          <th>E_prot_acf</th>
          <th>e_prot_cs</th>
          <th>E_prot_cs</th>
          <th>sph_ps</th>
          <th>sph_acf</th>
          <th>sph_cs</th>
          <th>e_sph_ps</th>
          <th>e_sph_acf</th>
          <th>e_sph_cs</th>
          <th>h_ps</th>
          <th>fa_prob_ps</th>
          <th>hacf</th>
          <th>gacf</th>
          <th>hcs</th>
        </tr>
        <tr>
          <th>target_id</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>891901</th>
          <td>5.583862</td>
          <td>51.574947</td>
          <td>5.641521</td>
          <td>0.451109</td>
          <td>0.538044</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.013094</td>
          <td>0.013094</td>
          <td>621.412430</td>
          <td>773.889578</td>
          <td>620.957800</td>
          <td>245.146024</td>
          <td>101.483976</td>
          <td>224.734810</td>
          <td>388.571741</td>
          <td>1.759694e-169</td>
          <td>0.277619</td>
          <td>0.109637</td>
          <td>0.012586</td>
        </tr>
        <tr>
          <th>1162339</th>
          <td>0.493096</td>
          <td>-1.000000</td>
          <td>0.976043</td>
          <td>0.000351</td>
          <td>0.000351</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.011880</td>
          <td>0.011880</td>
          <td>462.872324</td>
          <td>-1.000000</td>
          <td>578.779362</td>
          <td>359.874252</td>
          <td>-1.000000</td>
          <td>430.008329</td>
          <td>371.694864</td>
          <td>3.758129e-162</td>
          <td>-1.000000</td>
          <td>-1.000000</td>
          <td>0.040937</td>
        </tr>
        <tr>
          <th>1163248</th>
          <td>5.791226</td>
          <td>59.625771</td>
          <td>3.136216</td>
          <td>0.005828</td>
          <td>0.005840</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.166361</td>
          <td>0.166361</td>
          <td>443.149604</td>
          <td>541.775945</td>
          <td>346.123281</td>
          <td>163.047747</td>
          <td>41.778081</td>
          <td>98.225272</td>
          <td>20.010528</td>
          <td>2.039567e-09</td>
          <td>0.271948</td>
          <td>0.135494</td>
          <td>0.580406</td>
        </tr>
        <tr>
          <th>1164583</th>
          <td>50.378386</td>
          <td>43.891695</td>
          <td>1.465304</td>
          <td>-1.000000</td>
          <td>-1.000000</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.579764</td>
          <td>0.579764</td>
          <td>1650.421415</td>
          <td>1642.510883</td>
          <td>667.192946</td>
          <td>484.602802</td>
          <td>463.437724</td>
          <td>370.658390</td>
          <td>12.330474</td>
          <td>4.415127e-06</td>
          <td>0.635193</td>
          <td>0.317102</td>
          <td>1.218906</td>
        </tr>
        <tr>
          <th>1433067</th>
          <td>47.138724</td>
          <td>-1.000000</td>
          <td>30.768920</td>
          <td>0.047102</td>
          <td>0.047197</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>2.141848</td>
          <td>2.141848</td>
          <td>1197.078140</td>
          <td>-1.000000</td>
          <td>1142.311679</td>
          <td>306.901676</td>
          <td>-1.000000</td>
          <td>360.490565</td>
          <td>20.918206</td>
          <td>8.228836e-10</td>
          <td>-1.000000</td>
          <td>-1.000000</td>
          <td>0.218161</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>12647815</th>
          <td>10.435607</td>
          <td>10.421169</td>
          <td>10.439005</td>
          <td>0.010425</td>
          <td>0.010446</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.052430</td>
          <td>0.052430</td>
          <td>4727.467867</td>
          <td>4731.485721</td>
          <td>4725.580181</td>
          <td>1638.084281</td>
          <td>1651.040028</td>
          <td>1635.984428</td>
          <td>321.261367</td>
          <td>3.005808e-140</td>
          <td>0.993603</td>
          <td>0.606440</td>
          <td>0.928269</td>
        </tr>
        <tr>
          <th>12737258</th>
          <td>40.589407</td>
          <td>-1.000000</td>
          <td>40.522208</td>
          <td>0.040555</td>
          <td>0.040637</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.877765</td>
          <td>0.877765</td>
          <td>2135.275789</td>
          <td>-1.000000</td>
          <td>2138.867175</td>
          <td>598.419531</td>
          <td>-1.000000</td>
          <td>592.453395</td>
          <td>39.599624</td>
          <td>6.340181e-18</td>
          <td>-1.000000</td>
          <td>-1.000000</td>
          <td>0.158801</td>
        </tr>
        <tr>
          <th>12784167</th>
          <td>0.612374</td>
          <td>12.709734</td>
          <td>18.235136</td>
          <td>0.000006</td>
          <td>0.000006</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.197108</td>
          <td>0.197108</td>
          <td>346.990379</td>
          <td>615.325577</td>
          <td>631.680180</td>
          <td>55.723119</td>
          <td>142.765932</td>
          <td>128.610360</td>
          <td>103.591522</td>
          <td>1.025118e-45</td>
          <td>0.000056</td>
          <td>0.082313</td>
          <td>0.722011</td>
        </tr>
        <tr>
          <th>12834290</th>
          <td>52.678504</td>
          <td>57.295905</td>
          <td>3.254078</td>
          <td>0.052611</td>
          <td>0.052717</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.124075</td>
          <td>0.124075</td>
          <td>528.655933</td>
          <td>527.046251</td>
          <td>361.159430</td>
          <td>89.142743</td>
          <td>76.276120</td>
          <td>70.506151</td>
          <td>15.638527</td>
          <td>1.615377e-07</td>
          <td>0.197379</td>
          <td>0.076179</td>
          <td>0.160712</td>
        </tr>
        <tr>
          <th>12834663</th>
          <td>0.339495</td>
          <td>-1.000000</td>
          <td>1.628611</td>
          <td>-1.000000</td>
          <td>-1.000000</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.041504</td>
          <td>0.041504</td>
          <td>712.198133</td>
          <td>-1.000000</td>
          <td>787.582801</td>
          <td>86.012201</td>
          <td>-1.000000</td>
          <td>160.792154</td>
          <td>6.598372</td>
          <td>1.362585e-03</td>
          <td>-1.000000</td>
          <td>-1.000000</td>
          <td>0.207903</td>
        </tr>
      </tbody>
    </table>
    <p>1991 rows × 20 columns</p>
    </div>



.. code:: ipython3

    df.to_csv ("training_features.csv")

Training and testing ROOSTER
----------------------------

Now that we have analysed a large sample of stars, we are able to use it
to train the random forest ROOSTER methodology (see Breton et al. 2021).
First, let’s (arbitrarily) divide our DataFrame into a training set and
a test set.

.. code:: ipython3

    df_train = df.sample (n=df.index.size//2, random_state=49458493) 
    df_test = df.loc[np.setdiff1d (df.index, df_train.index)]

The DataFrames let us obtain all the input we require to train and test
ROOSTER:

.. code:: ipython3

    (training_id, training_p_candidates, 
     training_features, feature_names) = sp.create_rooster_feature_inputs (df_train)
    (test_id, test_p_candidates, 
     test_features, test_feature_names) = sp.create_rooster_feature_inputs (df_test)

Now, let’s instantiate a new ROOSTER object. The main attributes of
ROOSTER are its two random forest classifiers, ``RotClass`` and
``PeriodSel``. The properties of these classifiers can be specified by
the user by passing the optional arguments of
``sklearn.ensemble.RandomForestClassifier`` to the created ROOSTER
instance.

.. code:: ipython3

    feature_names




.. parsed-literal::

    Index(['E_prot_acf', 'E_prot_cs', 'E_prot_ps', 'e_prot_acf', 'e_prot_cs',
           'e_prot_ps', 'e_sph_acf', 'e_sph_cs', 'e_sph_ps', 'fa_prob_ps', 'gacf',
           'h_ps', 'hacf', 'hcs', 'prot_acf', 'prot_cs', 'prot_ps', 'sph_acf',
           'sph_cs', 'sph_ps'],
          dtype='object')



.. code:: ipython3

    seed = 104359357
    chicken = sp.ROOSTER (n_estimators=100, random_state=np.random.RandomState (seed=seed))
    chicken.RotClass, chicken.PeriodSel




.. parsed-literal::

    (RandomForestClassifier(random_state=RandomState(MT19937) at 0x133CCD040),
     RandomForestClassifier(random_state=RandomState(MT19937) at 0x133CCD040))



The training is performed as follows:

.. code:: ipython3

    chicken.train (training_id, training_p_candidates,
                   training_features, feature_names=feature_names,
                   catalog='santos-19-21', verbose=True)


.. parsed-literal::

    Training RotClass with 392 stars with detected rotation and 493 without detected rotation.
    Training PeriodSel with 392 stars.


Once properly trained, ROOSTER performances can be assessed with our
test set:

.. code:: ipython3

    results = chicken.test (test_id, test_p_candidates, test_features, 
                            feature_names=test_feature_names, 
                            catalog='santos-19-21', verbose=True)


.. parsed-literal::

    Testing RotClass with 380 stars with detected rotation and 502 without detected rotation.
    Testing PeriodSel with 380 stars.


The score obtained during the test set can be accessed through the
``getScore`` function, as well as the number of elements used for the
training and the test steps.

.. code:: ipython3

    chicken.getScore ()




.. parsed-literal::

    (0.9263038548752834, 0.9315789473684211)



.. code:: ipython3

    chicken.getNumberEltTrain ()




.. parsed-literal::

    (885, 392)



.. code:: ipython3

    chicken.getNumberEltTest ()




.. parsed-literal::

    (882, 380)



The :math:`P_\mathrm{rot}` computed by ROOSTER for the test set are
returned when calling the function and it can be interesting to plot the
distribution to compare it to the reference catalog values.

.. code:: ipython3

    prot_rooster = results[3]
    prot_ref = sp.get_prot_ref (results[2], catalog='santos-19-21')

Let’s take a look at the corresponding histogram

.. code:: ipython3

    fig, ax = plt.subplots (1, 1)
    
    bins = np.linspace (0, 80, 20, endpoint=False)
    
    ax.hist (prot_rooster, bins=bins, color='darkorange', label='ROOSTER')
    ax.hist (prot_ref, bins=bins, facecolor='none',
            edgecolor='black', label='Ref')
    
    ax.set_xlabel (r'$P_\mathrm{rot}$ (day)')
    ax.set_ylabel (r'Number of stars')
    
    ax.legend ()




.. parsed-literal::

    <matplotlib.legend.Legend at 0x1335b7af0>




.. image:: rooster_training_framework_files/rooster_training_framework_35_1.png


It can also be instructive to compare directly the ROOSTER results to
the reference values.

.. code:: ipython3

    fig, (ax, ax0) = plt.subplots (1, 2, figsize=(6, 4), 
                                   width_ratios=[0.8, 0.2],
                                   sharey=True)
    
    ax.scatter (prot_ref, (prot_rooster - prot_ref) / prot_ref * 100, 
                color='darkorange', s=3, marker="o")
    
    ax0.hist ((prot_rooster - prot_ref) / prot_ref * 100, 
              bins=np.linspace (-20, 20, 31), orientation="horizontal",
              color="darkorange")
    
    ax.set_xlabel (r'$P_\mathrm{rot, true}$ (day)')
    ax.set_ylabel (r"$\delta P_\mathrm{rot}$ (%)")
    
    ax.axhline (0, ls="--", color="grey")
    
    ax.set_ylim (-10, 10)
    
    ax0.set_xlim (0, 200)
    ax0.set_xlabel (r"$N_\mathrm{stars}$")




.. parsed-literal::

    Text(0.5, 0, '$N_\\mathrm{stars}$')




.. image:: rooster_training_framework_files/rooster_training_framework_37_1.png


Finally, let’s save our trained ROOSTER instance to be able to use it
again later (for example in the next tutorial notebook !)

.. code:: ipython3

    chicken.save ('rooster_instances/rooster_tutorial')

