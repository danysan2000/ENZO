#
#  Library-makefile fur submodule `examples' of enzo
#



# -- Archive Configuration --

AR              = ar    # make sure this is gnu-ar (/tools/bin/ar)
ARFLAGS         = rc 



NEPOMUKDIR      = ../nepomuk
#SNNSDIR      = ../../../snns_new/trunk/kernel/sources

SNNSDIR = ../$(SNNSINC)

ENZO_DIR  = ..




CC     = gcc
CFLAGS =  -I$(SNNSINC) -I$(NEPOMUKDIR) -I$(ENZO_DIR)  -D LINUX



LIB     = libexamples.a
OBJECTS = my_module.o



# ------------------------------------------------------------------------------

all:  opt

debug:  $(LIB)
debug:= CFLAGS += -ggdb -Wall

opt:  $(LIB)
opt:= CFLAGS += -O4


$(LIB): $(LIB)($(OBJECTS))
	$(AR) $(ARFLAGS) $@ $?


$(LIB)(%.o):%.o
	@true


#eof
