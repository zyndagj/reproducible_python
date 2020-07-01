#!/usr/bin/env python

import numpy as np
import summarize

def test_true():
	assert True == True

def test_gen_numbers_5():
	assert len(summarize.gen_numbers(5)) == 5
def test_gen_numbers_10():
	assert len(summarize.gen_numbers(10)) == 10

import pytest

@pytest.mark.parametrize("n", [5, 10])
def test_gen_numbers_len(n):
	assert len(summarize.gen_numbers(n)) == n

def test_gen_numbers_5_type():
	for n in summarize.gen_numbers(5):
		assert isinstance(n, np.int64)

def test_gen_numbers_5_vals_seed():
	np.random.seed(5)
	assert np.all(summarize.gen_numbers(5) == [99, 78, 61, 16, 73])

def test_summarize_custom():
	assert summarize.summarize([1,1,1,1,1]) == 1

def test_summarize_seed():
	np.random.seed(5)
	numbers = summarize.gen_numbers(5)
	assert summarize.summarize(numbers) == np.mean([99,78,61,16,73])
