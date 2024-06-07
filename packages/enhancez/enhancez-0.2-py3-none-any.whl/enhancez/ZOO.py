#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'''
.. module:: enhancez
   :platform: Unix, Windows
   :synopsis: This is the main module for enhancez.

.. moduleauthor:: Lalith Kumar Shiyam Sundar  <lalith.shiyamsundar@meduniwien.ac.at>

'''

# Import necessary libraries

import streamlit as st


def run():
    image_url="https://github.com/ENHANCE-PET/.github/blob/main/profile/EANM-ENHANCE-PET-Reveal.gif?raw=true"
    st.image(image_url, use_column_width='auto')


if __name__ == '__main__':
    run()
