#!/usr/bin/perl

# Purpose: This script provides information about the Milky Way,
# prints it to the console, and saves it to a file.
# File Name: milky_way_info_commented.pl

# Use strict and warnings to catch common coding errors
use strict;
use warnings;

# Information about the Milky Way
my $milky_way_name = "Milky Way";
my $milky_way_type = "Barred Spiral Galaxy";
my $milky_way_age  = "Approximately 13.6 billion years (it is thought)";

# Print information to the console
print "Welcome to the Milky Way Information Script!\n";
print "Name: $milky_way_name\n";
print "Type: $milky_way_type\n";
print "Age:  $milky_way_age\n";

# Writing information to a file

# Specify the output file name
my $output_file = "milky_way_info.txt";

# Open a file for writing or die with an error message if unsuccessful
open(my $fh, '>', $output_file) or die "Could not open file '$output_file' $!";

# Print Milky Way information to the file using the file handle ($fh)
print $fh "Milky Way Information:\n";
print $fh "Name: $milky_way_name\n";
print $fh "Type: $milky_way_type\n";
print $fh "Age: $milky_way_age\n";

# Close the file handle to release the file resource
close $fh;

# Print a message indicating that the information has been saved to the file
print "Milky Way information has been saved to $output_file\n";
