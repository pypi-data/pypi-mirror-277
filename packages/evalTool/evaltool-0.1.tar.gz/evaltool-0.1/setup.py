from setuptools import setup, find_packages

setup(
    name='evalTool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit', 'json5','aider-chat','deepeval','python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'create_custom_metrics=validation.create_custom_metrics:create_custom_metric',
            'custom_metrics=validation.custom_metrics:view_custom_metrics',
            'add_metric=validation.add_custom_metric:add_custom_metric',
            'manage_metrics=validation.manage_metrics:main'
        ]
    },
    author='Validation_team',
    author_email='vidhjain@deloitte.com',
    description='Validation framework with feedback loop',
    url='https://github.com/Deloitte-US/RAG_Validation_Framework',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)