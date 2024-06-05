from ipyweb.app import app
from ipyweb.singleton import singleton
from ipyweb.contracts.ipywebController import ipywebController
from ipyweb.pywebview.windows import windows


class ipyweb(ipywebController, metaclass=singleton):
    def version(self, window, args):
        try:

            return self.success('Version GET successful', {
                'ver': app.ver,
                'version': app.version
            })
        except Exception as e:
            return self.error(f'Version GET error:{e}')

    def create_window(self, window, args):
        try:
            if type(args) != dict:
                return self.error('Parameter incorrect')
            args['target'] = True
            if args.get('url', '') == '' and args.get('html', '') == '':
                return self.error('Parameter[html or url] must be set')
            flag = windows().run(args)
            if type(flag) == str:
                return self.error(flag)
            return self.success('Window create successful')
        except Exception as e:
            return self.error(f'Window create error:{e}')

    def set_title(self, window, args):
        try:
            if type(args) == str:
                title = args
            elif type(args) == dict:
                title = args.get('title', '')
            else:
                return self.error('Parameter[title] must be set')
            window.set_title(title)
            return self.success('Title set successfully')
        except Exception as e:
            return self.error(f'Title set error:{e}')

    def change_url(self, window, args):
        try:
            if type(args) == str:
                url = args
            elif type(args) == dict:
                url = args.get('url', '')
            else:
                return self.error('Parameter[url] must be set')
            window.load_url(url)
            return self.success('Url change successfully')
        except Exception as e:
            return self.error(f'Url change Error:{e}')

    def load_css(self, window, args):
        try:
            if type(args) == str:
                css = args
            elif type(args) == dict:
                css = args.get('css', '')
            else:
                return self.error('Parameter[css] must be set')
            window.load_css(css)
            return self.success('Css load successfully')
        except Exception as e:
            return self.error(f'Css load error:{e}')

    def load_html(self, window, args):
        try:
            if type(args) == str:
                html = args
            elif type(args) == dict:
                html = args.get('html', '')
            else:
                return self.error('Parameter[html] must be set')
            window.load_html(html)
            return self.success('Html load successfully')
        except Exception as e:
            return self.error(f'Html load error:{e}')

    def evaluate_js(self, window, args):
        try:
            if type(args) == str:
                js = args
            elif type(args) == dict:
                js = args.get('js', '')
            else:
                return self.error('Parameter[js] must be set')
            window.evaluate_js(js)
            return self.success('Js evaluate successfully')
        except Exception as e:
            return self.error(f'Js evaluate error:{e}')

    def destroy(self, window, args):
        try:
            window.destroy()
            return self.success('Window destroy successfully')
        except Exception as e:
            return self.error(f'Window destroy error:{e}')

    def hide(self, window, args):
        try:
            window.hide()
            return self.success('Window hide successfully')
        except Exception as e:
            return self.error(f'Window hide error:{e}')

    def show(self, window, args):
        try:
            window.show()
            return self.success('Window show successfully')
        except Exception as e:
            return self.error(f'Window show error:{e}')

    def minimize(self, window, args):
        try:
            window.restore()
            window.minimize()
            return self.success('Window minimize successfully')
        except Exception as e:
            return self.error(f'Window minimize error:{e}')

    def screens(self, window, args):
        try:
            import webview
            screens = webview.screens
            width, height = screens[0].width, screens[0].height
            return self.success('Screens GET successfully', {'width': width, 'height': height})
        except Exception as e:
            return self.error(f'Screens GET error:{e}')

    def toggle_fullscreen(self, window, args):
        try:
            window.toggle_fullscreen()
            return self.success('Fullscreen toggle successfully')
        except Exception as e:
            return self.error(f'Fullscreen toggle error:{e}')

    def move(self, window, args):
        try:
            if type(args) == dict:
                x = args.get('x', 0)
                y = args.get('y', 0)
            else:
                return self.error('Parameter[x and y] must be set')
            window.move(x, y)
            return self.success('Window move successfully')
        except Exception as e:
            return self.error(f'Window move error:{e}')

    def resize(self, window, args):
        try:
            if type(args) == dict:
                width = args.get('width', 0)
                height = args.get('height', 0)
            else:
                return self.error('Parameter[width and height] must be set')
            window.resize(width, height)
            return self.success('Window resize successfully')
        except Exception as e:
            return self.error(f'Window resize error:{e}')

    def open_file_dialog(self, window, args):
        try:
            import webview
            if type(args) != dict:
                return self.error('Parameter incorrect')
            file_type = args.get('file_type', 'Image Files (*.bmp;*.jpg;*.gif)')
            file_types = (file_type, 'All files (*.*)')
            allow_multiple = args.get('allow_multiple', True)
            files = window.create_file_dialog(
                dialog_type=webview.OPEN_DIALOG,
                allow_multiple=allow_multiple,
                file_types=file_types
            )

            return self.success('open_file_dialog successfully', {files: files})
        except Exception as e:
            return self.error(f'open_file_dialog error:{e}')

    def save_file_dialog(self, window, args):
        try:
            import webview
            if type(args) != dict:
                return self.error('保存文件参数异常')
            directory = args.get('directory', '/')
            filename = args.get('filename', 'file')
            allow_multiple = args.get('allow_multiple', False)
            files = window.create_file_dialog(
                dialog_type=webview.SAVE_DIALOG,
                directory=directory,
                allow_multiple=allow_multiple,
                save_filename=filename
            )
            return self.success('save_file_dialog successfully', {files: files})
        except Exception as e:
            return self.error(f'save_file_dialog error:{e}')
