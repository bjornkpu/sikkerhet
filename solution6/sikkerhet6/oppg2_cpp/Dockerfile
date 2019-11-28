FROM archlinux/base
RUN pacman -Sy --noconfirm clang cmake make
WORKDIR /home
COPY ./ /home
CMD ./run
