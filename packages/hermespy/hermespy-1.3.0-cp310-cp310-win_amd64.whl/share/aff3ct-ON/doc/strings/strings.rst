.. ------------------------------------------------ factory Launcher parameters

.. |factory::Launcher::p+cde-type,C| replace::
   Select the channel code family to simulate.

.. |factory::Launcher::p+type| replace::
   Select the type of simulation (or communication chain skeleton).

.. |factory::Launcher::p+prec,p| replace::
   Specify the representation of the real numbers in the receiver part of the
   chain.

.. |factory::Launcher::help,h| replace::
   Print the help with all the required (denoted as ``{R}``) and optional
   arguments. The latter change depending on the selected simulation type and
   code.

.. |factory::Launcher::Help,H| replace::
   Print the help like with the ``--help, -h`` parameter plus advanced arguments
   (denoted as ``{A}``).

.. |factory::Launcher::version,v| replace::
   Print informations about the version of the source code and compilation
   options.

.. |factory::Launcher::except-no-bt| replace::
   Disable the backtrace display when running an exception.

.. |factory::Launcher::except-a2l| replace::
   Enhance the backtrace when displaying exception. This change the program
   addresses into filenames and lines. It may take some seconds to do this work.

.. |factory::Launcher::no-legend| replace::
   Disable the legend display (remove all the lines beginning by the ``#``
   character).

.. |factory::Launcher::full-legend| replace::
   Display the legend with all modules details when launching the simulation.

.. |factory::Launcher::no-colors| replace::
   Disable the colors in the shell.

.. |factory::Launcher::keys,k| replace::
   Display the parameter keys in the help.

.. ---------------------------------------------- factory Simulation parameters

.. |factory::Simulation::p+meta| replace::
   Add meta-data at the beginning of the |AFF3CT| standard output (INI format is
   used). The value of the parameter will be affected to the *title* meta-data
   and the *command line* will be added.

.. |factory::Simulation::p+stop-time| replace::
   Set the maximum time (in seconds) to simulate per noise point. When a noise
   point reaches the maximum time limit, the simulation is stopped. 0 value
   means no limit.

.. |factory::Simulation::p+max-fra,n| replace::
   Set the maximum number of frames to simulate per noise point. When a noise
   point reaches the maximum frame limit, the simulation is stopped. 0 value
   means no limit.

.. |factory::Simulation::p+crit-nostop| replace::
   Stop only the current noise point instead of the whole simulation.

.. |factory::Simulation::p+dbg| replace::
   Enable the debug mode. This print the input and the output frames after each
   task execution.

.. |factory::Simulation::p+dbg-hex| replace::
   Enable the debug mode and **print values in the hexadecimal format**. This
   mode is useful for having a fully accurate representation of floating
   numbers.

.. |factory::Simulation::p+dbg-prec| replace::
   Enable the debug mode and **set the decimal precision** (number of digits for
   the decimal part) of the floating-point elements.

.. |factory::Simulation::p+dbg-limit,d| replace::
   Enable the debug mode and **set the max number of elements** to display per
   frame. 0 value means there is no dump limit.

.. |factory::Simulation::p+dbg-fra| replace::
   Enable the debug mode and **set the max number of frames** to display. 0
   value means there is no frame limit. By default, a task works on one frame at
   a time.

.. |factory::Simulation::p+stats| replace::
   Display statistics for each task. Those statistics are shown after each
   simulated |SNR| point.

.. |factory::Simulation::p+threads,t| replace::
   Specify the number of threads used in the simulation. The 0 default value
   will automatically set the number of threads to the hardware number of
   threads available on the machine.

.. |factory::Simulation::p+seed,S| replace::
   Set the |PRNG| seed used in the Monte Carlo simulation.

.. |factory::Simulation::p+inter-fra,F| replace::
   Set the number of frames to process for each task execution.

.. ---------------------------------------------------- factory BFER parameters

.. |factory::BFER::p+coset,c| replace::
   Enable the *coset* approach.

.. |factory::BFER::p+sequence-path| replace::
   Export the simulated sequence in Graphviz format at the given path.

.. |factory::BFER::p+err-trk| replace::
   Track the erroneous frames. When an error is found, the information bits from
   the source, the codeword from the encoder and the applied noise from the
   channel are dumped in several files.

.. |factory::BFER::p+err-trk-rev| replace::
   Replay dumped frames. By default this option reverts the ``--sim-err-trk``
   parameter by replaying the erroneous frames that have been dumped.

.. |factory::BFER::p+err-trk-path| replace::
   Specify the base path for the ``--sim-err-trk`` and ``--sim-err-trk-rev``
   parameters.

.. |factory::BFER::p+err-trk-thold| replace::
   Specify a threshold value in number of erroneous bits before which a frame is
   dumped.

.. |factory::BFER::p+coded| replace::
   Enable the coded monitoring.

.. |factory::BFER::p+sigma| replace::
   Show the standard deviation (:math:`\sigma`) of the Gaussian/Normal
   distribution in the terminal.

.. |factory::BFER::p+mutinfo| replace::
   Enable the computation of the mutual information (|MI|).

.. |factory::BFER::p+red-lazy| replace::
   Enable the lazy synchronization between the various monitor threads.

.. |factory::BFER::p+red-lazy-freq| replace::
   Set the time interval (in milliseconds) between the synchronizations of the
   monitor threads.

.. |factory::BFER::p+mpi-comm-freq| replace::
   Set the time interval (in milliseconds) between the |MPI| communications.
   Increase this interval will reduce the |MPI| communications overhead.

.. ------------------------------------------------ factory BFER_ite parameters

.. |factory::BFER_ite::p+ite,I| replace::
   Set the number of global iterations between the demodulator and the decoder.

.. |factory::BFER_ite::p+crc-earlyt| replace::
   Enable to use the CRC to early terminate (if possible) the turbo decoding
   process. It should reduce the simulation time in high SNR zones.

.. ------------------------------------------------ factory BFER_std parameters

.. ---------------------------------------------------- factory EXIT parameters

.. |factory::EXIT::p+siga-range| replace::
   Set the sigma range used in |EXIT| charts (|MATLAB| style:
   "0.5:2.5,2.55,2.6:0.05:3" with a default step of 0.1).

.. |factory::EXIT::p+siga-min,a| replace::
   Set the sigma minimum value used in |EXIT| charts.

.. |factory::EXIT::p+siga-max,A| replace::
   Set the sigma maximum value used in |EXIT| charts.

.. |factory::EXIT::p+siga-step| replace::
   Set the sigma step value used in |EXIT| charts.

.. ------------------------------------------------- factory Channel parameters

.. |factory::Channel::p+fra-size,N| replace::
   Set the number of symbols by frame.

.. |factory::Channel::p+type| replace::
   Select the channel type.

.. |factory::Channel::p+implem| replace::
   Select the implementation of the algorithm to generate the noise.

.. |factory::Channel::p+path| replace::
   Give the path to a file containing the noise.

.. |factory::Channel::p+blk-fad| replace::
   Set the block fading policy for the Rayleigh channel.

.. |factory::Channel::p+seed,S| replace::
   Set the seed used to initialize the |PRNG|.

.. |factory::Channel::p+add-users| replace::
   Add all the users (= frames) before generating the noise.

.. |factory::Channel::p+complex| replace::
   Enable complex noise generation.

.. |factory::Channel::p+gain-occur| replace::
   Give the number of times a gain is used on consecutive symbols. It is used in
   the ``RAYLEIGH_USER`` channel while applying gains read from the given file.

.. --------------------------------------------------- factory Codec parameters

.. ----------------------------------------------- factory Codec_BCH parameters

.. ---------------------------------------------- factory Codec_LDPC parameters

.. --------------------------------------------- factory Codec_polar parameters

.. ------------------------------------------ factory Codec_polar_MK parameters

.. ------------------------------------------------ factory Codec_RA parameters

.. ---------------------------------------- factory Codec_repetition parameters

.. ------------------------------------------------ factory Codec_RS parameters

.. ----------------------------------------------- factory Codec_RSC parameters

.. -------------------------------------------- factory Codec_RSC_DB parameters

.. --------------------------------------------- factory Codec_turbo parameters

.. ------------------------------------------ factory Codec_turbo_DB parameters

.. ------------------------------------- factory Codec_turbo_product parameters

.. ------------------------------------------- factory Codec_uncoded parameters

.. --------------------------------------------------- factory Coset parameters

.. |factory::Coset::p+size,N| replace::
   Set the frame size.

.. |factory::Coset::p+type| replace::
   Set the coset type.

.. ----------------------------------------------------- factory CRC parameters

.. |factory::CRC::p+info-bits,K| replace::
   Set the number of generated bits (information bits :math:`K`, the CRC is not
   included).

.. |factory::CRC::p+type,p+poly| replace::
   Select the |CRC| type you want to use among the predefined (or not)
   polynomials.

.. |factory::CRC::p+implem| replace::
   Select the |CRC| implementation you want to use.

.. |factory::CRC::p+size| replace::
   Size the |CRC| (divisor size in bits minus one), required if you selected an
   unknown |CRC|.

.. ------------------------------------------------- factory Decoder parameters

.. |factory::Decoder::p+cw-size,N| replace::
   Set the codeword size :math:`N`.

.. |factory::Decoder::p+info-bits,K| replace::
   Set the number of information bits :math:`K`.

.. |factory::Decoder::p+type,D| replace::
   Select the decoder algorithm.

.. |factory::Decoder::p+implem| replace::
   Select the implementation of the decoder algorithm.

.. |factory::Decoder::p+hamming| replace::
   Compute the `Hamming distance`_ instead of the `Euclidean distance`_ in the
   |ML| and Chase decoders.

.. |factory::Decoder::p+flips| replace::
   Set the maximum number of bit flips in the decoding algorithm.

.. |factory::Decoder::p+seed| replace::
   Specify the decoder |PRNG| seed (if the decoder uses one).

.. --------------------------------------------- factory Decoder_BCH parameters

.. |factory::Decoder_BCH::p+corr-pow,T| replace::
   Set the correction power of the |BCH| decoder. This value corresponds to the
   number of errors that the decoder is able to correct.

.. -------------------------------------------- factory Decoder_LDPC parameters

.. |factory::Decoder_LDPC::p+h-path| replace::
   Give the path to the :math:`H` parity matrix. Support the AList and the |QC|
   formats.

.. |factory::Decoder_LDPC::p+ite,i| replace::
   Set the maximal number of iterations in the |LDPC| decoder.

.. |factory::Decoder_LDPC::p+off| replace::
   Set the offset used in the |OMS| update rule.

.. |factory::Decoder_LDPC::p+mwbf-factor| replace::
   Give the weighting factor used in the |MWBF| algorithm.

.. |factory::Decoder_LDPC::p+norm| replace::
   Set the normalization factor used in the |NMS| update rule.

.. |factory::Decoder_LDPC::p+no-synd| replace::
   Disable the syndrome detection, all the |LDPC| decoding iterations will be
   performed.

.. |factory::Decoder_LDPC::p+synd-depth| replace::
   Set the number of iterations to process before enabling the syndrome
   detection. In some cases, it can help to avoid false positive detections.

.. |factory::Decoder_LDPC::p+simd| replace::
   Select the |SIMD| strategy.

.. |factory::Decoder_LDPC::p+min| replace::
   Define the :math:`\min^*` operator approximation used in the |AMS| update
   rule.

.. |factory::Decoder_LDPC::p+h-reorder| replace::
   Specify the order of execution of the |CNs| in the decoding process depending
   on their degree.

.. |factory::Decoder_LDPC::p+ppbf-proba| replace::
   Give the probabilities of the Bernouilli distribution of the |PPBF|.
   The number of given values must be equal to the biggest variable node degree
   plus two.

.. ---------------------------------------------- factory Decoder_NO parameters

.. ------------------------------------------- factory Decoder_polar parameters

.. |factory::Decoder_polar::p+ite,i| replace::
   Set the number of decoding iterations in the |SCAN| decoder.

.. |factory::Decoder_polar::p+lists,L| replace::
   Set the number of lists to maintain in the |SCL| and |A-SCL| decoders.

.. |factory::Decoder_polar::p+simd| replace::
   Select the |SIMD| strategy.

.. |factory::Decoder_polar::p+polar-nodes| replace::
   Set the rules to enable in the tree simplifications process. This parameter
   is compatible with the |SC| ``FAST``, the |SCL| ``FAST``, |SCL|-MEM ``FAST``,
   the |A-SCL| ``FAST`` and the the |A-SCL|-MEM ``FAST`` decoders.

.. |factory::Decoder_polar::p+partial-adaptive| replace::
   Select the partial adaptive (|PA-SCL|) variant of the |A-SCL| decoder (by
   default the |FA-SCL| is selected).

.. |factory::Decoder_polar::p+no-sys| replace::
   Enable non-systematic encoding.

.. ---------------------------------------- factory Decoder_polar_MK parameters

.. |factory::Decoder_polar_MK::p+lists,L| replace::
   Set the number of lists to maintain in the |SCL| decoder.

.. |factory::Decoder_polar_MK::p+node-type| replace::
   Select the type of computations to make in the decoding functions.

.. ---------------------------------------------- factory Decoder_RA parameters

.. |factory::Decoder_RA::p+ite,i| replace::
   Set the number of iterations to perform in the decoder.

.. -------------------------------------- factory Decoder_repetition parameters

.. |factory::Decoder_repetition::p+no-buff| replace::
   Do not suppose a buffered encoding.

.. ---------------------------------------------- factory Decoder_RS parameters

.. |factory::Decoder_RS::p+corr-pow,T| replace::
   Set the correction power of the |RS| decoder. This value corresponds to the
   number of symbols errors that the decoder is able to correct.

.. --------------------------------------------- factory Decoder_RSC parameters

.. |factory::Decoder_RSC::p+simd| replace::
   Select the |SIMD| strategy.

.. |factory::Decoder_RSC::p+max| replace::
   Select the approximation of the :math:`\max^*` operator used in the trellis
   decoding.

.. |factory::Decoder_RSC::p+no-buff| replace::
   Do not suppose a buffered encoding.

.. |factory::Decoder_RSC::p+poly| replace::
   Set the polynomials describing |RSC| code, should be of the form "{A,B}".

.. |factory::Decoder_RSC::p+std| replace::
   Select a standard.

.. ------------------------------------------ factory Decoder_RSC_DB parameters

.. |factory::Decoder_RSC_DB::p+max| replace::
   Select the approximation of the :math:`\max^*` operator used in the trellis
   decoding.

.. |factory::Decoder_RSC_DB::p+no-buff| replace::
   Do not suppose a buffered encoding.

.. ------------------------------------------- factory Decoder_turbo parameters

.. |factory::Decoder_turbo::p+ite,i| replace::
   Set the maximal number of iterations in the Turbo decoder.

.. |factory::Decoder_turbo::p+sc| replace::
   Enable the Self-Corrected (|SCo|) decoder.

.. |factory::Decoder_turbo::p+json| replace::
   Enable the |JSON| output trace.

.. |factory::Decoder_turbo::p+crc-start| replace::
   Set the first iteration to start the |CRC| checking.

.. ---------------------------------------- factory Decoder_turbo_DB parameters

.. |factory::Decoder_turbo_DB::p+ite,i| replace::
   Set the maximal number of iterations in the Turbo decoder.

.. |factory::Decoder_turbo_DB::p+crc-start| replace::
   Set the first iteration to start the |CRC| checking.

.. ----------------------------------- factory Decoder_turbo_product parameters

.. |factory::Decoder_turbo_product::p+ite,i| replace::
   Set the number of iterations in the turbo decoding process.

.. |factory::Decoder_turbo_product::p+alpha| replace::
   Give the *weighting factor* alpha, one by half iteration (so twice more than
   the number of iterations).

.. |factory::Decoder_turbo_product::p+beta| replace::
   Give the *reliability factor* beta, one by half iteration (so twice more than
   the number of iterations).

.. |factory::Decoder_turbo_product::p+p| replace::
   Set the number of *least reliable positions*.

.. |factory::Decoder_turbo_product::p+t| replace::
   Set the *number of test vectors*. A value of 0 means equal to :math:`2^p`
   where :math:`p` is the number of least reliable positions.

.. |factory::Decoder_turbo_product::p+c| replace::
   Set the *number of competitors*. A value of 0 means that the latter is set
   to the number of test vectors, 1 means only the decided word.

.. |factory::Decoder_turbo_product::p+ext| replace::
   Extend the code with parity bits.

.. |factory::Decoder_turbo_product::p+cp-coef| replace::
   Give the 5 ``CP`` constant coefficients :math:`a, b, c, d, e`.

.. ------------------------------------------------- factory Encoder parameters

.. |factory::Encoder::p+info-bits,K| replace::
   Set the number of information bits :math:`K`.

.. |factory::Encoder::p+cw-size,N| replace::
   Set the codeword size :math:`N`.

.. |factory::Encoder::p+type| replace::
   Select the encoder type.

.. |factory::Encoder::p+path| replace::
   Set the path to a file containing one or more codewords, to use with the
   ``USER`` encoder.

.. |factory::Encoder::p+start-idx| replace::
   Give the start index to use in the ``USER`` encoder. It is the index of the
   first codeword to read from the given file.

.. |factory::Encoder::p+seed,S| replace::
   Set the seed used to initialize the |PRNG|.

.. --------------------------------------------- factory Encoder_BCH parameters

.. |factory::Encoder_BCH::p+simd| replace::
   Select the |SIMD| strategy.

.. -------------------------------------------- factory Encoder_LDPC parameters

.. |factory::Encoder_LDPC::p+h-path| replace::
   Set the path to the :math:`H` matrix (AList formated file, required by the
   ``LDPC_H`` encoder).

.. |factory::Encoder_LDPC::p+g-path| replace::
   Give the path to the :math:`G` generator matrix in an AList or |QC| formated
   file.

.. |factory::Encoder_LDPC::p+h-reorder| replace::
   Specify if the |CNs| from :math:`H` have to be reordered, ``NONE``: do
   nothing (default), ``ASC``: from the smallest to the biggest |CNs|, ``DSC``:
   from the biggest to the smallest |CNs|.

.. |factory::Encoder_LDPC::p+g-method| replace::
   Specify the method used to build the :math:`G` generator matrix from the
   :math:`H` parity matrix when using the ``LDPC_H`` encoder.

.. |factory::Encoder_LDPC::p+g-save-path| replace::
   Set the file path where the :math:`G` generator matrix will be saved (AList
   file format). To use with the ``LDPC_H`` encoder.

.. ---------------------------------------------- factory Encoder_NO parameters

.. |factory::Encoder_NO::p+info-bits,K| replace::
   Set the number of information bits :math:`K`.

.. |factory::Encoder_NO::p+type| replace::
   Select the encoder type.

.. ------------------------------------------- factory Encoder_polar parameters

.. |factory::Encoder_polar::p+no-sys| replace::
   Enable non-systematic encoding. By default the encoding process is
   systematic.

.. ---------------------------------------- factory Encoder_polar_MK parameters

.. |factory::Encoder_polar_MK::p+sys| replace::
   Enable systematic encoding. By default the encoding process is
   non-systematic.

.. ---------------------------------------------- factory Encoder_RA parameters

.. -------------------------------------- factory Encoder_repetition parameters

.. |factory::Encoder_repetition::p+no-buff| replace::
   Disable the buffered encoding.

.. ---------------------------------------------- factory Encoder_RS parameters

.. --------------------------------------------- factory Encoder_RSC parameters

.. |factory::Encoder_RSC::p+no-buff| replace::
   Disable the buffered encoding.

.. |factory::Encoder_RSC::p+poly| replace::
   Set the polynomials that define the |RSC| code (or the trellis structure).
   The expected form is :math:`\{A,B\}` where :math:`A` and :math:`B` are given
   in octal.

.. |factory::Encoder_RSC::p+std| replace::
   Select a standard: set automatically some parameters (can be overwritten by
   user given arguments).

.. ------------------------------------------ factory Encoder_RSC_DB parameters

.. |factory::Encoder_RSC_DB::p+std| replace::
   Select a standard.

.. |factory::Encoder_RSC_DB::p+no-buff| replace::
   Disable the buffered encoding.

.. ------------------------------------------- factory Encoder_turbo parameters

.. |factory::Encoder_turbo::p+json-path| replace::
   Select the file path to dump the encoder and decoder internal values (in
   |JSON| format).

.. ---------------------------------------- factory Encoder_turbo_DB parameters

.. ----------------------------------- factory Encoder_turbo_product parameters

.. |factory::Encoder_turbo_product::p+ext| replace::
   Extend the *sub-encoder* codeword with a parity bit in order to increase the
   distance of the code.

.. --------------------------------------------- factory Interleaver parameters

.. --------------------------------------------------- factory Modem parameters

.. |factory::Modem::p+fra-size,N| replace::
   Set the number of symbols by frame.

.. |factory::Modem::p+type| replace::
   Select the modulation type.

.. |factory::Modem::p+implem| replace::
   Select the |modem| implementation.

.. |factory::Modem::p+bps| replace::
   Set the number of bits used to generate a symbol (|BPS|).

.. |factory::Modem::p+const-path| replace::
   Give the path to the ordered modulation symbols (constellation), to use with
   the ``USER`` |modem|.

.. |factory::Modem::p+cb-path| replace::
   Give the path to the codebook, to use with the ``SCMA`` |modem|.

.. |factory::Modem::p+cpm-std| replace::
   Set the |CPM| parameters according to a standard.

.. |factory::Modem::p+cpm-L| replace::
   Set the |CPM| *pulse width* (also called *memory depth*).

.. |factory::Modem::p+cpm-k| replace::
   Set the |CPM| *index numerator*.

.. |factory::Modem::p+cpm-p| replace::
   Set the |CPM| *index denominator*.

.. |factory::Modem::p+cpm-upf| replace::
   Select the symbol upsampling factor in the |CPM|.

.. |factory::Modem::p+cpm-map| replace::
   Select the |CPM| *symbols mapping layout*.

.. |factory::Modem::p+cpm-ws| replace::
   Select the |CPM| *wave shape*.

.. |factory::Modem::p+max| replace::
   Select the approximation of the :math:`\max^*` operator used in the |PAM|,
   |QAM|, |PSK|, |CPM| and user demodulators.

.. |factory::Modem::p+no-sig2| replace::
   Turn off the division by :math:`\sigma^2` in the demodulator where
   :math:`\sigma` is the Gaussian noise variance.

.. |factory::Modem::p+psi| replace::
   Select the :math:`\psi` function used in the |SCMA| demodulator.

.. |factory::Modem::p+ite| replace::
   Set the number of iterations in the |SCMA| demodulator.

.. |factory::Modem::p+rop-est| replace::
   Set the number of known bits for the |ROP| estimation in the |OOK|
   demodulator on an optical channel.

.. ------------------------------------------------- factory Monitor parameters

.. -------------------------------------------- factory Monitor_BFER parameters

.. |factory::Monitor_BFER::p+info-bits,K| replace::
   Set the number of bits to check.

.. |factory::Monitor_BFER::p+max-fe,e| replace::
   Set the maximum number of frame errors to simulated for each noise point.

.. |factory::Monitor_BFER::p+max-fra,n| replace::
   Set the maximum number of frames to simulate for each noise point.

.. |factory::Monitor_BFER::p+err-hist| replace::
   Enable the construction of the errors per frame histogram. Set also the
   maximum number of bit errors per frame included in the histogram (0 means no
   limit).

.. |factory::Monitor_BFER::p+err-hist-path| replace::
   Path to the output histogram. When the files are dumped, the current noise
   value is added to this name with the ``.txt`` extension.

.. -------------------------------------------- factory Monitor_EXIT parameters

.. |factory::Monitor_EXIT::p+size,K| replace::
   Set the number of bits to check.

.. |factory::Monitor_EXIT::p+trials,n| replace::
   Set the number of frames to simulate per :math:`\sigma A` value.

.. ---------------------------------------------- factory Monitor_MI parameters

.. |factory::Monitor_MI::p+fra-size,N| replace::
   Select the frame size for the mutual information computation.

.. |factory::Monitor_MI::p+trials,n| replace::
   Set the number of frames to simulate.

.. ----------------------------------------------- factory Puncturer parameters

.. |factory::Puncturer::p+info-bits,K| replace::
   Set the number of information bits :math:`K`.

.. |factory::Puncturer::p+fra-size,N| replace::
   Set the frame size :math:`N`. This is not necessarily the codeword size if a
   puncturing pattern is used.

.. |factory::Puncturer::p+type| replace::
   Select the puncturer type.

.. ------------------------------------------ factory Puncturer_LDPC parameters

.. |factory::Puncturer_LDPC::p+cw-size,N_cw| replace::
   Select the codeword size :math:`N`.

.. |factory::Puncturer_LDPC::p+pattern| replace::
   Give the puncturing pattern following the |LDPC| code.

.. ----------------------------------------- factory Puncturer_polar parameters

.. ----------------------------------------- factory Puncturer_turbo parameters

.. |factory::Puncturer_turbo::p+pattern| replace::
   Define the puncturing pattern.

.. |factory::Puncturer_turbo::p+tail-length| replace::
   Set the total number of tail bits at the end of the frame.

.. |factory::Puncturer_turbo::p+no-buff| replace::
   Do not suppose a buffered encoding.

.. -------------------------------------- factory Puncturer_turbo_DB parameters

.. ----------------------------------------------- factory Quantizer parameters

.. |factory::Quantizer::p+size,N| replace::
   Set the number of real to quantize.

.. |factory::Quantizer::p+type| replace::
   Select the quantizer type.

.. |factory::Quantizer::p+implem| replace::
   Select the implementation of the quantizer.

.. |factory::Quantizer::p+dec| replace::
   Set the position of the decimal point in the quantified representation.

.. |factory::Quantizer::p+bits| replace::
   Set the number of bits used in the fixed-point representation.

.. |factory::Quantizer::p+range| replace::
   Select the min/max bounds for the ``CUSTOM`` quantizer.

.. ---------------------------------------------------- factory Sink parameters

.. |factory::Sink::p+info-bits,K| replace::
   Select the number of information bits :math:`K`.

.. |factory::Sink::p+type| replace::
   Select the sink type.

.. |factory::Sink::p+implem| replace::
   Select the implementation of the sink.

.. |factory::Sink::p+path| replace::
   Set the path to a file to write the :math:`K` bits, to use with the
   ``USER_BIN`` source type.

.. -------------------------------------------------- factory Source parameters

.. |factory::Source::p+info-bits,K| replace::
   Select the number of information bits :math:`K`.

.. |factory::Source::p+type| replace::
   Method used to generate the :math:`K` information bits.

.. |factory::Source::p+implem| replace::
   Select the implementation of the algorithm to generate the information bits.

.. |factory::Source::p+path| replace::
   Set the path to a file containing one or more frames (informations bits), to
   use with the ``USER`` or ``USER_BIN`` source type.

.. |factory::Source::p+start-idx| replace::
   Give the start index to use in the ``USER`` source type. It is the index of
   the first frame to read from the given file.

.. |factory::Source::p+seed,S| replace::
   Set the seed used to initialize the |PRNGs|.

.. |factory::Source::p+no-reset| replace::
   Do not reset the source (start to the beginning) if the file reach |EOF| and
   pad with zeros after |EOF| (work only for ``USER_BIN`` source type).

.. |factory::Source::p+fifo| replace::
   If the FIFO (or pipe) reach the end, then reset the |EOF| flag and retry to
   read in loop.

.. ------------------------------------ factory Frozenbits_generator parameters

.. |factory::Frozenbits_generator::p+info-bits,K| replace::
   Select the number of information bits :math:`K`.

.. |factory::Frozenbits_generator::p+cw-size,N| replace::
   Select the codeword size :math:`N`.

.. |factory::Frozenbits_generator::p+noise| replace::
   Select the noise for which the frozen bits will be optimized.

.. |factory::Frozenbits_generator::p+gen-method| replace::
   Select the frozen bits generation method.

.. |factory::Frozenbits_generator::p+awgn-path| replace::
   Set the path to a file or a directory containing the best channels to select
   the frozen bits.

.. |factory::Frozenbits_generator::p+dump-path| replace::
   Set the path to store the best channels.

.. |factory::Frozenbits_generator::p+pb-path| replace::
   Set the path of the polar bounds code generator (generates best channels to
   use).

.. --------------------------------- factory Frozenbits_generator_MK parameters

.. |factory::Frozenbits_generator_MK::p+info-bits,K| replace::
   Select the number of information bits :math:`K`.

.. |factory::Frozenbits_generator_MK::p+cw-size,N| replace::
   Select the codeword size :math:`N`.

.. |factory::Frozenbits_generator_MK::p+noise| replace::
   Select the noise for which the frozen bits will be optimized.

.. |factory::Frozenbits_generator_MK::p+gen-method| replace::
   Select the frozen bits generation method.

.. |factory::Frozenbits_generator_MK::p+awgn-path| replace::
   Set the path to a file or a directory containing the best channels to select
   the frozen bits.

.. |factory::Frozenbits_generator_MK::p+dump-path| replace::
   Set the path to store the best channels.

.. ---------------------------------------------- factory Polar_code parameters

.. |factory::Polar_code::p+kernel| replace::
   Set the polar code kernel (squared matrix only).

.. |factory::Polar_code::p+path| replace::
   Set the path to a file containing the polar code description (kernels
   definition and stages).

.. ------------------------------------------ factory Flip_and_check parameters

.. |factory::Flip_and_check::p+| replace::
   Enable the |FNC| post processing technique.

.. |factory::Flip_and_check::p+size| replace::
   Set the size (in bit) of the extrinsic for the |FNC| processing.

.. |factory::Flip_and_check::p+q| replace::
   Set the search space for the |FNC| technique.

.. |factory::Flip_and_check::p+ite-m| replace::
   Set the first iteration at which the |FNC| is used.

.. |factory::Flip_and_check::p+ite-M| replace::
   Set the last iteration at which the |FNC| is used.

.. |factory::Flip_and_check::p+ite-s| replace::
   Set the iteration step for the |FNC| technique.

.. |factory::Flip_and_check::p+ite,i| replace::
   Set the maximal number of iterations in the Turbo decoding process.

.. |factory::Flip_and_check::p+crc-start| replace::
   Set the iteration to start the |CRC| checking.

.. --------------------------------------- factory Flip_and_check_DB parameters

.. ------------------------------------------ factory Scaling_factor parameters

.. |factory::Scaling_factor::p+type| replace::
   Select a scaling factor (|SF|) to be applied to the extrinsic values after
   each half iteration.

.. |factory::Scaling_factor::p+ite| replace::
   Set the number of iterations.

.. ------------------------------------------------ factory Terminal parameters

.. |factory::Terminal::p+type| replace::
   Select the terminal type (the format to display the results).

.. |factory::Terminal::p+no| replace::
   Disable completely the terminal report.

.. |factory::Terminal::p+freq| replace::
   Set the display frequency (refresh time) of the intermediate results in
   milliseconds. Setting 0 disables the display of the intermediate results.

.. ---------------------------------------- factory Interleaver_core parameters

.. |factory::Interleaver_core::p+size| replace::
   Select the number of symbols to interleave.

.. |factory::Interleaver_core::p+type| replace::
   Select the interleaver type.

.. |factory::Interleaver_core::p+path| replace::
   Set the file path to the interleaver |LUT| (to use with the ``USER``
   interleaver).

.. |factory::Interleaver_core::p+cols| replace::
   Specify the number of columns used for the ``RAND_COL``, ``ROW_COL`` or
   ``COL_ROW`` interleavers.

.. |factory::Interleaver_core::p+uni| replace::
   Enable to generate a new |LUT| *for each new frame* (i.e. uniform
   interleaver).

.. |factory::Interleaver_core::p+seed| replace::
   Select the seed used to initialize the |PRNG|.

.. |factory::Interleaver_core::p+read-order| replace::
   Change the read order of the ``COL_ROW`` and ``ROW_COL`` interleavers.

.. --------------------------------------------------- factory Noise parameters

.. |factory::Noise::p+noise-range,R| replace::
   Set the noise energy range to run in a |MATLAB| style vector.

.. |factory::Noise::p+noise-min,m| replace::
   Set the minimal noise energy value to simulate.

.. |factory::Noise::p+noise-max,M| replace::
   Set the maximal noise energy value to simulate.

.. |factory::Noise::p+noise-step,s| replace::
   Set the noise energy step between each simulation iteration.

.. |factory::Noise::p+pdf-path| replace::
   Give a file that contains |PDF| for different |ROP|.

.. |factory::Noise::p+noise-type,E| replace::
   Select the type of **noise** used to simulate.