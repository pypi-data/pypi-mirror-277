import setuptools

setuptools.setup(
    name='AuraAlerts',
    version='1.00',
    description='Simple Alerts For Desktop App Developers!!',
    long_description="==========================================================================================\n=It is a library that provides developers with GUI interfaces for the Python language     =\n==========================================================================================\n=The library is a good alternative to the default operating systems' messagebox or alerts =\n==========================================================================================\nUsage Examples:\n    Success Alerts:\n        AuraAlerts().Aa().success(title='hello',content='content') \n\n    Error Alerts:\n        AuraAlerts().Aa().error(title='hello',content='content') \n\n    Warn Alerts:\n        AuraAlerts().Aa().warn(title='hello',content='content') \n\n    Info Alerts:\n        AuraAlerts().Aa().info(title='hello',content='content') \nAa\n    Custom Alerts:\n        ``AuraAlerts().Aa().custom(title='title', content='content', buttonText, buttonColor='#e08aff', buttonHoverColor='#d561ff', imagePath='default image' , imgSize=(33,33), theme='light')`` \n        |__ Custom Alerts Is Customizable",
    long_description_content_type='text/markdown',
    author='abdrzakk',
    url='https://github.com/abdrzakk/AuraAlerts/',
    include_package_data=True,
    packages=setuptools.find_packages(),
    keywords=['AuraAlerts','Alerts','messagebox','alerts','aura'],
    requires=['customtkinter','Pillow','os'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ]
)