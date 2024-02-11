#
#  Library-makefile fur submodule `opt' of enzo
#



# -- Archive Configuration --

AR              = ar    # make sure this is gnu-ar (/tools/bin/ar)
ARFLAGS         = rc 


NEPOMUKDIR      = ../nepomuk
#SNNSDIR      = ../../../snns_new/trunk/kernel/sources

SNNSINC = ../$(SNNSDIR)


ENZO_DIR  = ..



CC      = gcc
CFLAGS  = -I$(ENZO_DIR)  -I$(NEPOMUKDIR) -I$(SNNSINC)  -D LINUX
 
LIB     = libopt.a
OBJECTS = prune.o relearn.o cleanup.o \
          nullWeg.o adapPrune.o jogWeights.o \
          learnSNNS.o   learnCV.o learnINIT.o 



# ------------------------------------------------------------------------------

all: opt


debug:  $(LIB)
debug:= CFLAGS += -ggdb -Wall

opt:  $(LIB)
opt:= CFLAGS += -O4



$(LIB): $(LIB)($(OBJECTS))
	$(AR) $(ARFLAGS) $@ $?


$(LIB)(%.o):%.o
	@true


#eof

