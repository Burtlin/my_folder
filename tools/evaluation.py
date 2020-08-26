import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import figure

def plt_confusion_matrix(cm, title='', classes=None, x_label=None, y_label=None, figsize=(14, 12), fontsize=35, cmap=plt.cm.Blues):
    '''plot confusion matrix
    
    Args:
        cm (numpy.ndarray): a confusion matrix.
        classes (list): list of classification name
        title (str)
        
    Retruns:
        fig (matplotlib.figure.Figure)
    '''
    if not (classes or x_label or y_label):
        classes = range(len(cm))
    if classes is not None:
        x_label = classes
        y_label = classes
    cm2 = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    print("ACC:" + format(sum(cm.diagonal()) / np.sum(cm)*100, '.2f'))
    
    fig = figure(figsize=figsize, facecolor='w')
    plt.imshow(cm2, interpolation='nearest', cmap=cmap, vmin=0, vmax=1)
    plt.title(title, fontsize=20)
    plt.colorbar()
    
    tick_marks = np.arange(len(x_label))
    plt.xticks(tick_marks, x_label, fontsize=20, color='#0b6008')
    plt.yticks(tick_marks, y_label, fontsize=20, color='#0b6008')

    thresh = cm.max() / 2. ; fmt = 'd'
    thresh2 = .5 ; fmt2 = '.2f'
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        text = '0.00' if np.isnan(cm[i, j]) else format(cm[i, j], fmt)
        text2 = '0.00' if np.isnan(cm2[i, j]) else format(cm2[i, j], fmt2)
        plt.text(j, i - 0.1, text,
                 horizontalalignment="center",
                 color="white" if cm2[i, j] > thresh2 else "red",
                 fontsize=fontsize)
        plt.text(j, i + 0.1, '(' + text2 + ')',
                 horizontalalignment="center",
                 color="white" if cm2[i, j] > thresh2 else "red",
                 fontsize=fontsize)
    plt.ylabel('True label', fontsize=20, color='#ca7b62')
    plt.xlabel('Predicted label', fontsize=20, color='#ca7b62')
    plt.text(0, -0.55, "ACC:" + format(sum(cm.diagonal()) / np.sum(cm)*100, '.2f'), horizontalalignment='center')
    return fig


if __name__ == '__main__':
    from sklearn.metrics import confusion_matrix
    y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
    y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
    cm = confusion_matrix(y_actu, y_pred)
    plt_cm = plt_confusion_matrix(cm, classes=['A', 'B', 'C'], fontsize=20, title='Example')
    # plt.savefig('Example.png')
    plt.show()