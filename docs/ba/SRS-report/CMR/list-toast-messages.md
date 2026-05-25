# BẢNG THÔNG BÁO LỖI & THÔNG BÁO HỆ THỐNG
## Phân hệ Báo cáo | Hệ thống MBFS

> Tài liệu này tổng hợp toàn bộ các thông báo (Toast, Alert, Popup) được sử dụng trong phân hệ Báo cáo.
> Đây là nguồn tham chiếu duy nhất cho QC và Dev khi triển khai thông báo hệ thống.

---

## 1. Toast Messages

Toast hiển thị ở góc trên bên phải màn hình, tự động biến mất sau 3–5 giây.

| Mã | Trường hợp | Tiêu đề | Nội dung thông báo | Loại | Tham chiếu CF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T01** | Lập báo cáo + Lưu nháp | Thành công | Đã lập báo cáo thành công | 🟢 Success | CF_01 |
| **T02** | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success | CF_01, CF_03 |
| **T03** | Chỉnh sửa báo cáo + Lưu nháp | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success | CF_03 |
| **T04** | Kết xuất (Xuất báo cáo) thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success | CF_04, CF_07 |
| **T05** | Lỗi hệ thống (không kết nối được server, gọi API thất bại, lưu nháp thất bại, nộp thất bại, xuất báo cáo thất bại) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error | CF_01–CF_07 |
| **T06** | Chọn Phạm vi báo cáo đã có bản ghi được tạo bởi người dùng khác trong kỳ hiện tại | Báo cáo đã được lập | Báo cáo cho [Phạm vi báo cáo] đã chọn đã được lập bởi [Tên người lập] | 🔴 Error | CF_01, CF_02 |
| **T07** | Lưu nháp khi tất cả trường đều trống (chưa nhập bất kỳ dữ liệu nào) | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error | CF_01, CF_03 |
| **T08** | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success | CF_08 |
| **T09** | Phê duyệt báo cáo thành công | Thành công | Đã phê duyệt báo cáo thành công | 🟢 Success | UC367-372 |
| **T10** | Từ chối báo cáo thành công | Thành công | Đã từ chối báo cáo thành công | 🟢 Success | UC367-372 |
| **T11** | Gửi yêu cầu chỉnh sửa thành công | Thành công | Đã gửi yêu cầu chỉnh sửa thành công | 🟢 Success | UC367-372 |
| **T12** | Race Condition: Trạng thái bản ghi đã thay đổi bởi luồng khác | Không thể thực hiện | Trạng thái báo cáo đã thay đổi. Vui lòng tải lại trang | 🔴 Error | UC367-372 |
| **T13** | Validation form: Phát hiện trường Email sai định dạng khi Nộp | Lỗi | Vui lòng kiểm tra lại các trường Email chưa đúng định dạng | 🔴 Error | UC035-040 |
| **T14** | Validation form: Phát hiện trường Số điện thoại sai định dạng khi Nộp | Lỗi | Vui lòng kiểm tra lại các trường Số điện thoại chưa đúng định dạng | 🔴 Error | UC035-040 |
| **T15** | Bảng động rỗng (0 dòng) khi Nộp báo cáo | Lỗi | Vui lòng nhập ít nhất 1 dòng dữ liệu | 🔴 Error | UC089-094, UC101-106... |
| **T16** | Thêm mới dòng dữ liệu khi bảng đã đạt giới hạn tối đa | Lỗi | Vượt quá số dòng tối đa cho phép (500) | 🔴 Error | UC089-094, UC113-118... |
| **T17** | Lỗi tạo mới khi Kỳ báo cáo đã tồn tại | Lỗi | Kỳ báo cáo đã tồn tại trong hệ thống. Vui lòng kiểm tra lại | 🔴 Error | UC041-046 |

---

## 2. Alert Messages (hiển thị trên popup, không tự biến mất)

| Mã | Trường hợp | Nội dung thông báo | Nút đi kèm | Tham chiếu CF |
| :--- | :--- | :--- | :--- | :--- |
| **A01** | Upload file nhập từ file: dữ liệu không khớp với Phạm vi báo cáo đã chọn | Dữ liệu không khớp với [Phạm vi báo cáo] đã chọn. Vui lòng kiểm tra lại. | — (giữ nguyên popup) | CF_02 |
| **A02** | Upload file nhập từ file: cấu trúc file không đúng template (file đúng định dạng nhưng khác template) | Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải. | — (giữ nguyên popup) | CF_02 |
| **A03** | Upload file nhập từ file: sai định dạng (không phải .docx/.xlsx) | Định dạng file không được hỗ trợ. Vui lòng sử dụng file template đã tải. | — (giữ nguyên popup) | CF_02 |
| **A04** | Upload file nhập từ file: file rỗng hoặc không đọc được | Không thể đọc file. Vui lòng kiểm tra lại file và thử lại. | — (giữ nguyên popup) | CF_02 |

---

## 3. Inline Validation Messages

| Mã | Trường hợp | Nội dung thông báo | Vị trí hiển thị | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- |
| **V01** | Trường bắt buộc bị bỏ trống (khi nhấn Lưu nháp hoặc Nộp) | Vui lòng nhập [tên trường] / Vui lòng chọn [tên trường] | Bên dưới trường thông tin, màu đỏ | CMR_05, CMR_06, CMR_07, CF_01, CF_03 |
| **V02** | Trường số: nhập ký tự không hợp lệ (chữ cái, ký tự đặc biệt ngoài `-`, `.`, `,`) | Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ | Bên dưới trường thông tin, màu đỏ | CMR_05 |
| **V03** | Trường số yêu cầu ≥ 0: nhập dấu trừ `-` | Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy | Bên dưới trường thông tin, màu đỏ | CMR_05 |
| **V04** | Trường số: sai cấu trúc (thừa dấu `.`, sai vị trí `,`, dấu liền kề, paste sai) | Định dạng số không hợp lệ | Bên dưới trường thông tin, màu đỏ | CMR_05 |
| **V05** | Số công văn: thiếu dấu `/` | Số công văn chưa đúng chuẩn, thiếu dấu "/" | Bên dưới trường thông tin, màu đỏ | CMR_13 |
| **V06** | Số công văn: thiếu dấu `-` | Số công văn chưa đúng chuẩn, thiếu dấu "-" | Bên dưới trường thông tin, màu đỏ | CMR_13 |
| **V07** | Số công văn: sai format tổng thể | Vui lòng nhập lại thông tin | Bên dưới trường thông tin, màu đỏ | CMR_13 |
| **V08** | Kinh phí quyết toán vượt kinh phí thực hiện (cross-field: cột (12)≤(9), (13)≤(10), (14)≤(11)) | Kinh phí quyết toán không được vượt kinh phí thực hiện | Bên dưới trường thông tin, màu đỏ | UC011-034 (B.4.3) |
| **V09** | Tổng kinh phí quyết toán vượt tổng kinh phí thực hiện | Tổng kinh phí quyết toán không được vượt kinh phí thực hiện | Bên dưới trường thông tin, màu đỏ | UC011-034 (B.4.3) |
| **V10** | Năm báo cáo đã có Bộ hồ sơ "Đã nộp" | Đã tồn tại báo cáo cho năm này | Bên dưới trường thông tin, màu đỏ | UC011-034 (B.4.2) |
| **V11** | Trường Tình hình thực hiện triển khai bỏ trống khi Nộp | Vui lòng nhập tình hình thực hiện triển khai | Bên dưới trường thông tin, màu đỏ | UC011-034 (B.4.4) |
| **V12** | Vốn đăng ký dự kiến ≤ 0 | Giá trị phải lớn hơn 0 | Bên dưới trường thông tin, màu đỏ | UC011-034 (A.IV.4) |
| **V13** | Trùng cặp Nhà đầu tư + Dự án trên cùng 1 báo cáo | Nhà đầu tư này đã được ghi nhận quan tâm đến dự án này | Bên dưới trường thông tin, màu đỏ | UC011-034 (A.IV.4) |
| **V14** | Năm báo cáo không đúng 4 chữ số hoặc > năm hiện tại −1 | Năm báo cáo không hợp lệ | Bên dưới trường thông tin, màu đỏ | UC011-034 (B.4.2) |
| **V15** | Diện tích đất vượt tổng diện tích quỹ đất dự án | Diện tích đất không được vượt tổng diện tích quỹ đất của dự án | Bên dưới trường thông tin, màu đỏ | UC011-034 (A.IV.4) |
| **V16** | Bảng động / Form rỗng khi Nộp (không có dữ liệu tối thiểu) | Vui lòng khai báo ít nhất 1 [đối tượng] trong kỳ báo cáo | Inline error hoặc Toast lỗi tùy UC | UC245-298. [đối tượng] thay đổi theo UC: KCN, KKT, chỉ tiêu, v.v. |
| **V17** | Trường số: vượt giới hạn phần nguyên hoặc thập phân | [Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân | Bên dưới trường thông tin, màu đỏ | CMR_05 |
| **V18** | Trường text/số: vượt max length | [Tên trường] không được vượt quá [maxlength] ký tự! | Bên dưới trường thông tin, màu đỏ | CMR_05, CMR_06 |
| **V19** | Trường text/số: chưa đủ min length | [Tên trường] nhập chưa đủ [minlength] ký tự! | Bên dưới trường thông tin, màu đỏ | CMR_05, CMR_06 |
| **V20** | Trường Mã: nhập khoảng trắng hoặc ký tự có dấu | Mã không bao gồm khoảng trắng và ký tự có dấu | Bên dưới trường thông tin, màu đỏ | CMR_19 |

---

## 4. Popup xác nhận (Confirmation Popup)

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút đi kèm | Tham chiếu CF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P01** | Xác nhận trước khi nộp báo cáo | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác." | [Xác nhận] *(chỉ active khi checkbox đã tích)* / [Hủy] / Icon Đóng (✕) | CF_01, CF_03 |
| **P02** | Cảnh báo dữ liệu chưa lưu khi điều hướng (Dirty Form Guard) | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] | CF_01, CF_03, CMR_14 |
| **P03** | Xung đột đồng thời — báo cáo đã được lập bởi NĐT khác (Case B - ĐTRNN) | Báo cáo đã được lập bởi nhà đầu tư khác | Báo cáo [Tên báo cáo] đã được lập bởi [Tên nhà đầu tư]. Vui lòng không lập lại báo cáo này. | [Đồng ý] / Icon Đóng (✕) | CF_01 |
| **P04** | Xác nhận trước khi xóa báo cáo | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] | CF_08 |

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-08 | 1.0 → 1.1 | V02–V07 (Inline Validation) | (Không có) | Thêm 6 mã: V02 (ký tự lạ trường số), V03 (số dương), V04 (sai format số), V05 (thiếu `/`), V06 (thiếu `-`), V07 (sai format công văn) | Đồng bộ với CMR_05, CMR_13 |
| 2026-05-08 | 1.0 → 1.1 | V08–V16 (Inline Validation) | (Không có) | Thêm 9 mã: V08 (cross-field kinh phí), V09 (tổng kinh phí), V10 (trùng năm), V11 (trường triển khai), V12 (vốn > 0), V13 (trùng NĐT), V14 (năm k hợp lệ), V15 (diện tích vượt), V16 (bảng rỗng khi Nộp) | Yêu cầu từ UC011-034, UC245-298 |
| 2026-05-18 | 1.1 -> 1.2 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.2 -> 1.3 | Bổ sung mã Toast (T09–T17) | Chỉ có T01–T08 | Thêm 9 mã: T09, T10, T11 (Duyệt/Từ chối), T12 (Race condition), T13, T14 (Email/SĐT), T15, T16 (Empty/Max table), T17 (Trùng kỳ) | Chuẩn hóa các Toast message rải rác ở từng file UC |
| 2026-05-18 | 1.3 -> 1.4 | Mô tả trường hợp T01, T03 | T01: "Lập báo cáo mới / Lưu nháp thành công"; T03: "Chỉnh sửa và lưu lại thành công" | T01: "Lập báo cáo + Lưu nháp"; T03: "Chỉnh sửa báo cáo + Lưu nháp" | Chuẩn hóa cách diễn đạt ngắn gọn, nhất quán |
| 2026-05-19 | 1.4 → 1.5 | V08, V09, V10, V11, V14 — Cột Áp dụng | UC011-034 (B.IV.2 / B.IV.3 / B.IV.4) | UC011-034 (B.4.2 / B.4.3 / B.4.4) | Đổi tên mã biểu theo quy ước mới |
| 2026-05-24 | 1.5 → 1.6 | V01 — Required message | *"Trường bắt buộc"* | *"Vui lòng nhập [tên trường]"* / *"Vui lòng chọn [tên trường]"* | Đồng bộ CMR v3.0 |
| 2026-05-24 | 1.5 → 1.6 | V04 — Sai định dạng số | *"Sai định dạng số."* | *"Định dạng số không hợp lệ"* (bỏ dấu `.`) | Đồng bộ CMR_05 v3.0 |
| 2026-05-24 | 1.5 → 1.6 | V08–V15 — Bỏ dấu `.` cuối | Có dấu `.` cuối message | Bỏ dấu `.` cuối toàn bộ (8 mã) | Quy tắc: inline error không có `.` cuối |
| 2026-05-24 | 1.5 → 1.6 | V17–V20 — Thêm mới | (Không có) | V17 (vượt numeric), V18 (vượt max length), V19 (thiếu min length), V20 (mã có dấu/trắng) | Đồng bộ CMR_05, CMR_06, CMR_19 v3.0 |
| 2026-05-24 | 1.6 → 1.7 | T05, T12, T17 — Bỏ dấu `.` cuối | Có dấu `.` cuối message | Bỏ dấu `.` cuối (3 mã Toast) | Đồng bộ rule: toast cũng không có `.` cuối |
