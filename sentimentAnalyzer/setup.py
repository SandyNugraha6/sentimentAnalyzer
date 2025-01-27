from setuptools import setup, find_packages  
  
setup(  
    name='sentiment_analysis_svm',  
    version='0.1',  
    packages=find_packages(),  
    install_requires=[  
        'joblib',  
        'scikit-learn',  
        'numpy',  
        'pandas',  
        'imbalanced-learn',  
        'matplotlib',  
        'seaborn'  
    ],  
    description='A simple sentiment analysis library using SVM.',  
    author='Your Name',  
    author_email='your.email@example.com',  
    url='https://github.com/SandyNugraha6/sentimentAnalyzer',  # Ganti dengan URL repositori Anda  
)  