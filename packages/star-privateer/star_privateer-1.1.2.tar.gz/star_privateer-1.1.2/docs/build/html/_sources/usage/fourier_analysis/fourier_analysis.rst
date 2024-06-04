Fourier analysis (MSAP4-01A)
============================

.. code:: ipython3

    import star_privateer as sp
    import plato_msap4_demonstrator_datasets.plato_sim_dataset as plato_sim_dataset

.. code:: ipython3

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

.. code:: ipython3

    sp.__version__




.. parsed-literal::

    '1.1.2'



K2: Rotation period analysis
----------------------------

.. code:: ipython3

    t, s, dt = sp.load_k2_example ()

.. code:: ipython3

    fig, ax = plt.subplots (1, 1, figsize=(8,4))
    
    ax.scatter (t[s!=0]-t[0], s[s!=0], color='black', 
                marker='o', s=1)
    
    ax.set_xlabel ('Time (day)')
    ax.set_ylabel ('Flux (ppm)')
    
    fig.tight_layout ()



.. image:: fourier_analysis_files/fourier_analysis_6_0.png


As we want to recover rotation periods below 45 days, we only consider
the section of the periodogram verifying
:math:`P < P_\mathrm{cutoff} = 60` days.

.. code:: ipython3

    pcutoff = 60

As a preprocessing step, we compute the Lomb-Scargle periodogram (in the
SAS framework, it will be directyly provided by MSAP1).

.. code:: ipython3

    p_ps, ls = sp.compute_lomb_scargle (t, s)

Now we perform the periodogram analysis.

.. code:: ipython3

    cond = p_ps < pcutoff
    (prot, e_p, E_p, 
     _, param, h_ps) = sp.compute_prot_err_gaussian_fit_chi2_distribution (p_ps[cond], ls[cond], pfa_threshold=1e-6, 
                                                                           plot_procedure=False,
                                                                           verbose=False)
    fig= sp.plot_ls (p_ps, ls, filename='figures/fourier_k2.png', param_profile=param, 
                     logscale=False, xlim=(0.1, 5))



.. image:: fourier_analysis_files/fourier_analysis_12_0.png


.. code:: ipython3

    IDP_SAS_PROT_FOURIER = sp.prepare_idp_fourier (param, h_ps, ls.size,
                                                  pcutoff=pcutoff, pthresh=None,
                                                  pfacutoff=1e-6)
    
    df = pd.DataFrame (data=IDP_SAS_PROT_FOURIER)
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
          <th>0</th>
          <th>1</th>
          <th>2</th>
          <th>3</th>
          <th>4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>1.393528</td>
          <td>0.001392</td>
          <td>0.001395</td>
          <td>438.472941</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>1</th>
          <td>0.779111</td>
          <td>0.000778</td>
          <td>0.000780</td>
          <td>368.082305</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>2</th>
          <td>2.787059</td>
          <td>0.002784</td>
          <td>0.002790</td>
          <td>291.548014</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>3</th>
          <td>2.683252</td>
          <td>0.002680</td>
          <td>0.002686</td>
          <td>85.520009</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>4</th>
          <td>0.225067</td>
          <td>0.000427</td>
          <td>0.000428</td>
          <td>43.158470</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>5</th>
          <td>0.129272</td>
          <td>0.000028</td>
          <td>0.000028</td>
          <td>33.369658</td>
          <td>3.219155e-15</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df.to_latex (buf='data_products/idp_sas_prot_fourier_k2_211015853.tex', 
                 formatters=['{:.2f}'.format, '{:.2f}'.format, '{:.2f}'.format,
                             '{:.2f}'.format, '{:.0e}'.format],  
                 index=False, header=False)
    np.savetxt ('data_products/IDP_SAS_PROT_FOURIER_K2.dat', 
                 IDP_SAS_PROT_FOURIER)

PLATO: Rotation period analysis
-------------------------------

The PLATO simulation below encompasses both rotational modulation and
low-frequency modulations due to activity. In order to analyse the
rotational signal, we first filter out frequencies above 60 days (in
PLATO, this will be done outside MSAP4).

.. code:: ipython3

    filename = sp.get_target_filename (plato_sim_dataset, '040', filetype='csv')
    t, s, dt = sp.load_resource (filename)
    s_filtered = sp.preprocess (t, s, cut=60)

.. code:: ipython3

    fig, ax = plt.subplots (1, 1, figsize=(8,4))
    
    ax.scatter (t[s!=0]-t[0], s[s!=0], color='black', 
                marker='o', s=1, label="Unfiltered")
    ax.scatter (t[s!=0]-t[0], s_filtered[s_filtered!=0], color='darkorange', 
                marker='o', s=1, label="Filtered")
    
    ax.set_xlabel ('Time (day)')
    ax.set_ylabel ('Flux (ppm)')
    
    ax.legend ()
    
    fig.tight_layout ()



.. image:: fourier_analysis_files/fourier_analysis_18_0.png


As we want to recover rotation periods below 60 days, we only consider
the section of the periodogram verifying
:math:`P < P_\mathrm{cutoff} = 60` days.

.. code:: ipython3

    pcutoff = 60

As a preprocessing step, we compute the Lomb-Scargle periodogram (in the
SAS framework, it will be directyly provided by MSAP1).

.. code:: ipython3

    p_ps, ls = sp.compute_lomb_scargle (t, s_filtered)

Now we perform the periodogram analysis.

.. code:: ipython3

    cond = p_ps < pcutoff
    (prot, e_p, E_p, 
     _, param, h_ps) = sp.compute_prot_err_gaussian_fit_chi2_distribution (p_ps[cond], 
                                                                           ls[cond], 
                                                                           pfa_threshold=1e-6,
                                                                           verbose=False)
    sp.plot_ls (p_ps, ls, filename='figures/fourier_plato_short.png', param_profile=param, 
                logscale=False, xlim=(1, pcutoff), 
                )
    IDP_SAS_PROT_FOURIER = sp.prepare_idp_fourier (param, h_ps, ls.size,
                                                  pcutoff=pcutoff, pthresh=None,
                                                  pfacutoff=1e-6)
    df = pd.DataFrame (data=IDP_SAS_PROT_FOURIER)
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
          <th>0</th>
          <th>1</th>
          <th>2</th>
          <th>3</th>
          <th>4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>25.714472</td>
          <td>0.025694</td>
          <td>0.025745</td>
          <td>28.380401</td>
          <td>4.726593e-13</td>
        </tr>
        <tr>
          <th>1</th>
          <td>26.704732</td>
          <td>0.026685</td>
          <td>0.026738</td>
          <td>17.165303</td>
          <td>3.509164e-08</td>
        </tr>
        <tr>
          <th>2</th>
          <td>23.942589</td>
          <td>0.023925</td>
          <td>0.023973</td>
          <td>15.850085</td>
          <td>1.307361e-07</td>
        </tr>
      </tbody>
    </table>
    </div>




.. image:: fourier_analysis_files/fourier_analysis_24_1.png


.. code:: ipython3

    df.to_latex (buf='data_products/idp_sas_prot_fourier_plato_040.tex', 
                 formatters=['{:.2f}'.format, '{:.2f}'.format, '{:.2f}'.format,
                             '{:.2f}'.format, '{:.0e}'.format],  
                 index=False, header=False)
    np.savetxt ('data_products/IDP_SAS_PROT_FOURIER_PLATO.dat', 
                 IDP_SAS_PROT_FOURIER)

PLATO: Long term modulation analysis
------------------------------------

This time, we are interested in recovering long term modulations. We
consider the section of the periodogram verifying
:math:`P > P_\mathrm{tresh} = 60` days.

.. code:: ipython3

    pthresh = 60

As a preprocessing step, we compute the Lomb-Scargle periodogram (in the
SAS framework, it will be directyly provided by MSAP1).

.. code:: ipython3

    p_ps, ls = sp.compute_lomb_scargle (t, s, normalisation="snr_flat")

Now we perform the periodogram analysis.

.. code:: ipython3

    (plongterm, e_p, E_p, 
     _, param, h_ps) = sp.compute_prot_err_gaussian_fit_chi2_distribution (p_ps[p_ps>pthresh], 
                                                                           ls[p_ps>pthresh], 
                                                                           pfa_threshold=1e-6, 
                                                                           verbose=False)
    fig = sp.plot_ls (p_ps, ls, filename='figures/fourier_plato_long.png', param_profile=param, 
                        logscale=False, xlim=(1,8*pthresh))
    IDP_SAS_LONGTERM_MODULATION_FOURIER = sp.prepare_idp_fourier (param, h_ps, ls.size,
                                                                  pcutoff=None, pthresh=pthresh,
                                                                  pfacutoff=1e-6)
    df = pd.DataFrame (data=IDP_SAS_LONGTERM_MODULATION_FOURIER)
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
          <th>0</th>
          <th>1</th>
          <th>2</th>
          <th>3</th>
          <th>4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>347.003860</td>
          <td>0.346584</td>
          <td>0.347278</td>
          <td>8.754753e+06</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>1</th>
          <td>693.938698</td>
          <td>0.693030</td>
          <td>0.694417</td>
          <td>2.280495e+06</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>2</th>
          <td>115.612182</td>
          <td>0.115417</td>
          <td>0.115648</td>
          <td>5.105828e+05</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>3</th>
          <td>86.663796</td>
          <td>0.086471</td>
          <td>0.086644</td>
          <td>3.620016e+05</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>4</th>
          <td>62.592651</td>
          <td>0.062019</td>
          <td>0.062142</td>
          <td>2.829973e+05</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>5</th>
          <td>231.113051</td>
          <td>0.230567</td>
          <td>0.231028</td>
          <td>2.553851e+05</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>6</th>
          <td>99.058919</td>
          <td>0.098854</td>
          <td>0.099052</td>
          <td>1.641647e+05</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>7</th>
          <td>77.045937</td>
          <td>0.076886</td>
          <td>0.077040</td>
          <td>1.452372e+05</td>
          <td>1.000000e-16</td>
        </tr>
        <tr>
          <th>8</th>
          <td>173.336225</td>
          <td>0.172940</td>
          <td>0.173286</td>
          <td>1.025115e+05</td>
          <td>1.000000e-16</td>
        </tr>
      </tbody>
    </table>
    </div>




.. image:: fourier_analysis_files/fourier_analysis_32_1.png


.. code:: ipython3

    df.to_latex (buf='data_products/idp_sas_longterm_modulation_fourier_plato_040.tex', 
                 formatters=['{:.2f}'.format, '{:.2f}'.format, '{:.2f}'.format,
                             '{:.2f}'.format, '{:.0e}'.format],  
                 index=False, header=False)
    np.savetxt ('data_products/IDP_SAS_LONGTERM_MODULATION_FOURIER_PLATO.dat', 
                 IDP_SAS_LONGTERM_MODULATION_FOURIER)

