import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .XPlotLibUtils import non_uniform_savgol, ryd_to_ev

class BandgapAnalyzer():
    def __init__(self):
        self.xes_exp_spectra = {}
        self.xes_calc_spectra = {}
        self.xas_exp_spectra = {}
        self.xas_calc_spectra = {}
        self.figsize = (12, 6)
        self.xes_xlims = None
        self.xas_xlims = None
        self.subplot_labels = [['XES' , 'XAS'], ['2nd der.', '2nd der.']]
        self.xes_arrow = None
        self.xas_arrow = None
        self.xes_line = None
        self.xas_line = None
        self.title = None

        self.gs_onsets = []
        self.es_onsets = []

    def __load_spectrum(self, path, names, skiprows, sep):
        headers = [[f'{header}_energy', f'{header}_intensity'] for header in names]
        headers = [item for sublist in headers for item in sublist]
        return pd.read_csv(path, sep=sep, skiprows=skiprows, header=None, names=headers)
    
    def __normalize(self, list):
        abs_max = max(max(list), -min(list))
        return [x/abs_max for x in list]
    
    
    def __find_onset(self, path, binding, fermi):
        df = pd.read_csv(path, sep='\\s+', header=None, names=['energy', 'intensity1', 'intensity2', 'intensity3'])
        onset = min(df.loc[df['intensity1']>0]['energy']) + (binding + fermi) * ryd_to_ev
        return onset

    """
    Load experimental spectra

    Parameters
    ----------
    path : str
        Path to the file containing the spectra
    type : str
        Type of the spectra. Must be either 'xes' or 'xas'
    names : list of str
        Names of the spectra
    skiprows : int, optional
        Number of rows to skip in the beginning of the file
    sep : str, optional
        Separator used in the file
    """
    def load_exp_spectra(self, path, type, names, skiprows=2, sep=','):        
        if type == 'xes':
            exp_spectra = self.xes_exp_spectra
        elif type == 'xas':
            exp_spectra = self.xas_exp_spectra
        else:
            raise ValueError('type must be either "xes" or "xas"')
        

        df = self.__load_spectrum(path, names, skiprows, sep)
        for name in names:
            exp_spectra[name] = df[[f'{name}_energy', f'{name}_intensity']]


    """
    Load calculated spectra

    Parameters
    ----------
    path : str
        Path to the file containing the spectra
    type : str
        Type of the spectra. Must be either 'xes' or 'xas'
    name : str
        Name of the spectra
    skiprows : int
        Number of rows to skip in the beginning of the file
    sep : str
        Separator used in the file
    """
    def load_calc_spectra(self, path, type, name, skiprows=1, sep=','):    
        if type == 'xes':
            calc_spectra = self.xes_calc_spectra
        elif type == 'xas':
            calc_spectra = self.xas_calc_spectra
        else:
            raise ValueError('type must be either "xes" or "xas"')

        df = self.__load_spectrum(path, [name], skiprows, sep)
        calc_spectra[name] = df


    """
    Smoothen the experimental spectra using a Savitzky-Golay filter. The smoothed data will shown in a plot with the option to show the onset region. The parameters set here will be used in the plot method.

    Parameters
    ----------  
    type : str
        Type of the spectra. Must be either 'xes' or 'xas'
    name : str
        Name of the spectra
    window : int
        Window length of datapoints. Must be odd and smaller than x
    poly : int
        The order of polynom used. Must be smaller than the window size
    onset_region : tuple of float, optional
        Tuple containing the start and end of the onset region
    show : bool, optional 
        If True, the smoothed data will be plotted
    """
    def smoothen(self, type, name, window, poly, onset_region = None, show = True):         
        if type == 'xes':
            exp_spectra = self.xes_exp_spectra
        elif type == 'xas':
            exp_spectra = self.xas_exp_spectra
        else:
            raise ValueError('type must be either "xes" or "xas"')

        x = exp_spectra[name][f'{name}_energy'].values
        y = exp_spectra[name][f'{name}_intensity'].values
        y_smoothed = non_uniform_savgol(x, y, window, poly)
        exp_spectra[name][f'{name}_smoothed_intensity'] = y_smoothed
        # take second derivative
        exp_spectra[name][f'{name}_smoothed_2nd'] = np.gradient(np.gradient(y_smoothed, x), x)


        # make sure onset region includes at least one data point
        if onset_region:
            if onset_region[0] > onset_region[1]:
                raise ValueError('The start of the onset region must be smaller than the end.')
            if onset_region[1] < min(x) or onset_region[0] > max(x):
                raise ValueError('The onset region is outside of the energy range.')

        if show:
            # plot the smoothed data
            if onset_region:
                fig, (ax, ax_onset) = plt.subplots(1,2, figsize=(10,6))
                ax_onset.set_xlim(onset_region)
                ax_onset.set_xlim(onset_region)
                y_onset = exp_spectra[name].loc[(exp_spectra[name][f'{name}_energy'] >= onset_region[0]) & (exp_spectra[name][f'{name}_energy'] <= onset_region[1]), f'{name}_intensity']
                ax_onset.set_ylim(min(y_onset), max(y_onset))
                ax_onset.plot(x, y, label='Raw data')
                ax_onset.plot(x, y_smoothed, label='Smoothed data')
                ax_onset.legend()
            else:
                fig, ax = plt.subplots()
            ax.plot(x, y, label='Raw data')
            ax.plot(x, y_smoothed, label='Smoothed data')
            ax.legend()

    """
    Set the title of the plot

    Parameters
    ----------
    title : str
        Title of the plot
    """
    def set_title(self, title):
        self.title = title


    """
    Set the figure size of the plot

    Parameters
    ----------
    figsize : tuple of float
        Tuple containing the width and height of the figure
    """
    def set_figsize(self, figsize):
        self.figsize = figsize


    """
    Set the x limits of the plot

    Parameters
    ----------
    xes_xlims : tuple of float
        Tuple containing the start and end of the x-axis for the XES spectra
    xas_xlims : tuple of float
        Tuple containing the start and end of the x-axis for the XAS spectra
    """
    def set_xlims(self, xes_xlims, xas_xlims):
        self.xes_xlims = xes_xlims
        self.xas_xlims = xas_xlims

    """
    Add an arrow to annotate the last/first peak of the 2nd derivative of XES/XAS spectra

    Parameters
    ----------
    type : str
        Type of the spectra. Must be either 'xes' or 'xas'
    xy : tuple of float
        Tuple containing the x and y coordinates of the peak
    xytext : tuple of float
        Tuple containing the x and y coordinates of the text
    text : str
        Text to be shown
    text_rot : float, optional
        Rotation of the text
    """
    def add_arrow(self, type, xy, xytext, text, text_rot = 0):
        if type == 'xes':
            self.xes_arrow = (xy, xytext, text, text_rot)
        elif type == 'xas':
            self.xas_arrow = (xy, xytext, text, text_rot)
        else:
            raise ValueError('type must be either "xes" or "xas"')


    """
    Add a vertical line to the plot with energy label

    Parameters
    ----------
    type : str
        Type of the spectra. Must be either 'xes' or 'xas'
    energy : float
        Energy of the line
    linestyle : str, optional
        Linestyle of the line
    color : str, optional
        Color of the line
    linewidth : float, optional
        Width of the line
    label : bool, optional
        If True, the energy will be shown as a label
    xytext : tuple of float, optional
        Tuple containing the x and y coordinates of the label
    """

    def add_line(self, type, energy, linestyle='--', color='black', linewidth=1, label=True, xytext=None):
        if type == 'xes':
            self.xes_line = (energy, linestyle, color, linewidth, label, xytext)
        elif type == 'xas':
            self.xas_line = (energy, linestyle, color, linewidth, label, xytext)
        else:
            raise ValueError('type must be either "xes" or "xas"')


    """
    Plot the spectra in four plots with the XES and XAS in the top row and their 2nd derivatives in the bottom row.

    Parameters
    ----------
    xes_exp_names : list of str
        Names of the experimental XES spectra
    xes_calc_names : list of str
        Names of the calculated XES spectra
    xas_exp_names : list of str
        Names of the experimental XAS spectra
    xas_calc_names : list of str
        Names of the calculated XAS spectra
    """
    def plot(self, xes_exp_names, xes_calc_names, xas_exp_names, xas_calc_names):
        fig, axes = plt.subplots(2,2, sharex='col', gridspec_kw={'height_ratios': [2, 1]}, figsize=self.figsize)

        # XES
        if self.xes_xlims:
            axes[0,0].set_xlim(self.xes_xlims)
            axes[1,0].set_xlim(self.xes_xlims)
        for xes_exp_name in xes_exp_names:
            axes[0,0].plot(self.xes_exp_spectra[xes_exp_name][f'{xes_exp_name}_energy'], self.__normalize(self.xes_exp_spectra[xes_exp_name][f'{xes_exp_name}_intensity']), label=xes_exp_name)
            axes[1,0].plot(self.xes_exp_spectra[xes_exp_name][f'{xes_exp_name}_energy'],  self.__normalize(self.xes_exp_spectra[xes_exp_name][f'{xes_exp_name}_smoothed_2nd']))
        for xes_calc_name in xes_calc_names:
            axes[0,0].plot(self.xes_calc_spectra[xes_calc_name][f'{xes_calc_name}_energy'], self.__normalize(self.xes_calc_spectra[xes_calc_name][f'{xes_calc_name}_intensity']), label=xes_calc_name)


        # XAS
        if self.xas_xlims:
            axes[0,1].set_xlim(self.xas_xlims)
            axes[1,1].set_xlim(self.xas_xlims)
        for xas_exp_name in xas_exp_names:
            axes[0,1].plot(self.xas_exp_spectra[xas_exp_name][f'{xas_exp_name}_energy'], self.__normalize(self.xas_exp_spectra[xas_exp_name][f'{xas_exp_name}_intensity']), label=xas_exp_name)
            axes[1,1].plot(self.xas_exp_spectra[xas_exp_name][f'{xas_exp_name}_energy'],  self.__normalize(self.xas_exp_spectra[xas_exp_name][f'{xas_exp_name}_smoothed_2nd']))
        for xas_calc_name in xas_calc_names:
            axes[0,1].plot(self.xas_calc_spectra[xas_calc_name][f'{xas_calc_name}_energy'], self.__normalize(self.xas_calc_spectra[xas_calc_name][f'{xas_calc_name}_intensity']), label=xas_calc_name)

        # remove space between subplots
        fig.subplots_adjust(wspace=0, hspace=0)

        if self.title:
            fig.suptitle(self.title, y = 0.95)

        for i in range(len(axes)):
            for j in range(len(axes[i])):
                ax = axes[i,j]
                # set ticks only on outside edges
                ax.minorticks_on()
                ax.tick_params(axis='x', which='both', bottom= (i==1), top=(i==0), labelbottom=(i==1))
                ax.tick_params(axis='y', which='both', left=(j==0), right=(j==1), labelleft=(j==0), labelright=(j==1))
                # remove last tick labels for left subplots
                if j == 0 and i == 0:
                    ax.set_xticks(ax.get_xticks()[:-1])
                

                # show text in corner
                ax.text(0.11/self.figsize[0], 1 - (1+i)*0.08/self.figsize[1], self.subplot_labels[i][j], size=11, ha='left', va='top', color='white', bbox=dict(facecolor='black', edgecolor='none', pad=3), transform=ax.transAxes)
                
                if i == 0: # spectra subplots
                    ax.legend(loc='upper right')                    
                else: # 2nd derivative subplots
                    # center 0 in y-axis
                    abs_max = max(-ax.get_ylim()[0], ax.get_ylim()[1])
                    ax.set_ylim(-abs_max, abs_max)

            # annotate last XES peak
            if self.xes_arrow:
                xy, xytext, text, text_rot = self.xes_arrow
                axes[1,0].annotate(text, xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05), ha='center', va='center', rotation=text_rot)

            if self.xes_line:
                energy, linestyle, color, linewidth, label, xytext = self.xes_line
                axes[0,0].axvline(x=energy, color=color, linestyle=linestyle, linewidth=linewidth)
                axes[1,0].axvline(x=energy, color=color, linestyle=linestyle, linewidth=linewidth)
                # add energy label
                if label:
                    xytext = xytext if xytext else (energy + 0.2, -0.7)
                    xy = (energy, xytext[1]) if xytext else (energy, -0.7)
                    axes[1,0].annotate(f'{energy} eV', xy=xy, xytext=xytext, ha='left')

            # annotate first XAS peak
            if self.xas_arrow:
                xy, xytext, text, text_rot = self.xas_arrow
                axes[1,1].annotate(text, xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05), ha='center', va='center', rotation=text_rot)

            if self.xas_line:
                energy, linestyle, color, linewidth, label, xytext = self.xas_line
                axes[0,1].axvline(x=energy, color=color, linestyle=linestyle, linewidth=linewidth)
                axes[1,1].axvline(x=energy, color=color, linestyle=linestyle, linewidth=linewidth)
                # add energy label
                if label:
                    xytext = xytext if xytext else (energy - 0.2, -0.7)
                    xy = (energy, xytext[1]) if xytext else (energy, -0.7)
                    axes[1,1].annotate(f'{energy} eV', xy=xy, xytext=xytext, ha='right')

    """
    Export 2nd derivative of XES and XAS spectra to csv files

    Parameters
    ----------
    path : str
        Path to the directory where the files will be saved
    name : str
        Name of the files (without extension)
    """
    def export_2nd_derivative(self, path, name):
        xes_2nd = pd.DataFrame()
        for xes_exp_name in self.xes_exp_spectra.keys():
            if f'{xes_exp_name}_smoothed_2nd' not in self.xes_exp_spectra[xes_exp_name].columns:
                print(f'No 2nd derivative found for {xes_exp_name}. Run smoothen method first, if you want to export the 2nd derivative.')
                continue
            xes_2nd[f'{xes_exp_name}_energy'] = self.xes_exp_spectra[xes_exp_name][f'{xes_exp_name}_energy']
            xes_2nd[f'{xes_exp_name}_2nd'] = self.xes_exp_spectra[xes_exp_name][f'{xes_exp_name}_smoothed_2nd']
        xes_2nd.to_csv(f'{path}/{name}_XES_2nd.csv', index=False)

        xas_2nd = pd.DataFrame()
        for xas_exp_name in self.xas_exp_spectra.keys():
            if f'{xas_exp_name}_smoothed_2nd' not in self.xas_exp_spectra[xas_exp_name].columns:
                print(f'No 2nd derivative found for {xas_exp_name}. Run smoothen method first, if you want to export the 2nd derivative.')
                continue
            xas_2nd[f'{xas_exp_name}_energy'] = self.xas_exp_spectra[xas_exp_name][f'{xas_exp_name}_energy']
            xas_2nd[f'{xas_exp_name}_2nd'] = self.xas_exp_spectra[xas_exp_name][f'{xas_exp_name}_smoothed_2nd']
        xas_2nd.to_csv(f'{path}/{name}_XAS_2nd.csv', index=False)

    """
    Load unbrodened spectra to determine core hole shift

    Parameters
    ----------
    dir : str
        Directory containing the spectra
    GS_file : str
        File containing the ground state XAS spectrum
    ES_file : str
        File containing the excited state XAS spectrum
    GS_binding : float
        Binding energy of the ground state
    GS_fermi : float
        Fermi energy of the ground state
    ES_fermi : float
        Fermi energy of the excited state
    """
    def load_unbroadend(self, dir, GS_file, ES_file, GS_binding, GS_fermi, ES_fermi):
        self.gs_onsets.append(self.__find_onset(f'{dir}/{GS_file}', GS_binding, GS_fermi))
        self.es_onsets.append(self.__find_onset(f'{dir}/{ES_file}', GS_binding, ES_fermi))

    """
    Calculate the core hole shift using all previously loaded unbrodened spectra.
    !Warning this might not be accurate!

    Returns
    -------
    float
        Core hole shift
    """
    def calc_core_hole_shift(self):
        return min(self.es_onsets) - min(self.gs_onsets)

    