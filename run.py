# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:11:49 2021

@author: win10
"""

from flaskblog import create_app

app = create_app()



if __name__ == '__main__':
    app.run(debug=True)
    