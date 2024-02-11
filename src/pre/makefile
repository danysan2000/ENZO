#
#  Library-makefile fur submodule `pre' of enzo
#



# -- Archive Configuration --

AR              = ar    # make sure this is gnu-ar (/tools/bin/ar)
ARFLAGS         = rc 


NEPOMUKDIR      = ../nepomuk
#SNNSDIR      = ../../../SNNSv4.1/kernel/sources
#SNNSDIR      = ../../../snns_new/trunk/kernel/sources
SNNSINC = ../$(SNNSDIR) 


ENZO_DIR  = ..



CC      = gcc
CFLAGS  =  -I$(ENZO_DIR) -I$(SNNSINC) -I$(NEPOMUKDIR) -D LINUX
 


LIB     = libpre.a
OBJECTS = genpopNepomuk.o initPop.o loadPop.o optInitPop.o loadSNNSPat.o\
          hiddenInitPop.o inputInit.o weightInit.o startPop.o initTrain.o	\


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
