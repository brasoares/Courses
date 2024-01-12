#!/usr/bin/perl

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
my $output_file = "milky_way_info.txt";

open(my $fh, '>', $output_file) or die "Could not open file '$output_file' $!";
print $fh "Milky Way Information:\n";
print $fh "Name: $milky_way_name\n";
print $fh "Type: $milky_way_type\n";
print $fh "Age: $milky_way_age\n";
close $fh;

print "Milky Way information has been saved to $output_file\n";
